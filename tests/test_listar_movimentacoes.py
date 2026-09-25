"""
Testes unitários para a funcionalidade de listagem de movimentações de estoque.
Issue #85 — Listar movimentações de estoque.

O que estes testes provam:
  1. list_inventory_movements retorna todas as movimentações em ordem decrescente de data.
  2. O dicionário gerado por movement_to_dict contém todos os campos obrigatórios.
  3. A rota GET /api/inventory/movements responde 200 com a lista serializada.
"""

from datetime import datetime

import pytest

from app.core.models import InventoryMovement, Product
from app.core.services.market_service import list_inventory_movements, movement_to_dict

# ---------------------------------------------------------------------------
# Helpers — objetos em memória (sem banco de dados)
# ---------------------------------------------------------------------------


def _make_product(product_id: int = 1, name: str = "Arroz 5 kg") -> Product:
    """Cria um Product sem persistência para uso nos testes."""
    product = Product.__new__(Product)
    product.id = product_id
    product.name = name
    product.description = "Arroz tipo 1"
    product.category = "Alimentos"
    product.price = 25.90
    product.stock = 100
    product.promotional = False
    return product


def _make_movement(
    movement_id: int,
    product: Product,
    movement_type: str,
    quantity: int,
    created_at: datetime,
) -> InventoryMovement:
    """Cria um InventoryMovement sem persistência para uso nos testes."""
    mov = InventoryMovement.__new__(InventoryMovement)
    mov.id = movement_id
    mov.product_id = product.id
    mov.type = movement_type
    mov.quantity = quantity
    mov.created_at = created_at
    mov.product = product
    return mov


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def sample_movements() -> list[InventoryMovement]:
    """
    Retorna 3 movimentações com datas distintas (mais antiga → mais recente)
    para validar ordenação decrescente.
    """
    product = _make_product()
    return [
        _make_movement(1, product, "ENTRY", 50, datetime(2025, 1, 10, 8, 0, 0)),
        _make_movement(2, product, "SALE", 5, datetime(2025, 1, 11, 14, 0, 0)),
        _make_movement(3, product, "ENTRY", 20, datetime(2025, 1, 12, 9, 0, 0)),
    ]


# ---------------------------------------------------------------------------
# Testes de list_inventory_movements
# ---------------------------------------------------------------------------


class TestListInventoryMovements:
    """
    Dado um conjunto de movimentações conhecidas,
    quando list_inventory_movements for chamada com uma sessão simulada,
    deve retornar os registros corretos ordenados por data decrescente.
    """

    def test_retorna_lista_com_todos_os_registros(
        self, sample_movements: list[InventoryMovement]
    ) -> None:
        """Prova: a função devolve o mesmo número de registros que foram inseridos."""

        class _FakeScalars:
            def all(self) -> list[InventoryMovement]:
                # simula ordem crescente vinda do banco; a função deve reordenar
                return list(reversed(sample_movements))

        class _FakeSession:
            def scalars(self, _stmt):  # noqa: ANN001
                return _FakeScalars()

        result = list_inventory_movements(_FakeSession())  # type: ignore[arg-type]
        assert len(result) == 3

    def test_ordenacao_decrescente_por_data(
        self, sample_movements: list[InventoryMovement]
    ) -> None:
        """
        Prova: o primeiro elemento da lista possui a data mais recente
        (ordem decrescente de created_at).
        """

        class _FakeScalars:
            def all(self) -> list[InventoryMovement]:
                return sample_movements  # entregue em ordem crescente

        class _FakeSession:
            def scalars(self, _stmt):  # noqa: ANN001
                return _FakeScalars()

        result = list_inventory_movements(_FakeSession())  # type: ignore[arg-type]
        dates = [m.created_at for m in result]
        assert dates == sorted(dates, reverse=True), (
            "As movimentações devem estar ordenadas da mais recente para a mais antiga."
        )

    def test_tipos_de_movimentacao_preservados(
        self, sample_movements: list[InventoryMovement]
    ) -> None:
        """Prova: os tipos das movimentações (ENTRY, SALE) são preservados sem alteração."""

        class _FakeScalars:
            def all(self) -> list[InventoryMovement]:
                return sample_movements

        class _FakeSession:
            def scalars(self, _stmt):  # noqa: ANN001
                return _FakeScalars()

        result = list_inventory_movements(_FakeSession())  # type: ignore[arg-type]
        types_found = {m.type for m in result}
        assert "ENTRY" in types_found
        assert "SALE" in types_found


# ---------------------------------------------------------------------------
# Testes de movement_to_dict
# ---------------------------------------------------------------------------


class TestMovementToDict:
    """
    Dado um InventoryMovement,
    quando movement_to_dict for chamado,
    deve retornar um dicionário com todos os campos obrigatórios e valores corretos.
    """

    def test_campos_obrigatorios_presentes(self) -> None:
        """Prova: o dicionário contém id, productId, type, quantity e createdAt."""
        product = _make_product()
        mov = _make_movement(
            movement_id=10,
            product=product,
            movement_type="ENTRY",
            quantity=30,
            created_at=datetime(2025, 6, 1, 12, 0, 0),
        )

        result = movement_to_dict(mov)

        assert set(result.keys()) >= {"id", "productId", "type", "quantity", "createdAt"}

    def test_valores_corretos_no_dicionario(self) -> None:
        """Prova: os valores do dicionário correspondem exatamente aos atributos do objeto."""
        product = _make_product(product_id=7, name="Feijão 1 kg")
        created = datetime(2025, 6, 15, 10, 30, 0)
        mov = _make_movement(
            movement_id=42,
            product=product,
            movement_type="SALE",
            quantity=3,
            created_at=created,
        )

        result = movement_to_dict(mov)

        assert result["id"] == 42
        assert result["productId"] == 7
        assert result["type"] == "SALE"
        assert result["quantity"] == 3
        assert result["createdAt"] == created.isoformat()

    def test_campo_product_contem_nome(self) -> None:
        """Prova: o dicionário inclui o nome do produto aninhado no campo 'product'."""
        product = _make_product(name="Leite Integral 1L")
        mov = _make_movement(
            movement_id=1,
            product=product,
            movement_type="ENTRY",
            quantity=10,
            created_at=datetime(2025, 1, 1),
        )

        result = movement_to_dict(mov)

        assert "product" in result
        assert result["product"]["name"] == "Leite Integral 1L"


# ---------------------------------------------------------------------------
# Teste de integração leve — rota HTTP
# ---------------------------------------------------------------------------


class TestRotaListarMovimentacoes:
    """
    Dado o servidor Flask em modo de teste com banco em memória,
    quando GET /api/inventory/movements for chamado,
    deve retornar status 200 com uma lista JSON.
    """

    def test_endpoint_retorna_200(self) -> None:
        """Prova: a rota existe e responde com 200 OK."""
        from app.core import create_app

        app = create_app()
        client = app.test_client()

        response = client.get("/api/inventory/movements")

        assert response.status_code == 200

    def test_endpoint_retorna_lista_json(self) -> None:
        """Prova: o corpo da resposta é uma lista JSON (podendo estar vazia)."""
        from app.core import create_app

        app = create_app()
        client = app.test_client()

        response = client.get("/api/inventory/movements")
        data = response.get_json()

        assert isinstance(data, list), "A resposta deve ser uma lista JSON."
