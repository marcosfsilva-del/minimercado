from app.features.filtro_promocoes.service import list_promotional_products


def test_existe_acao_ver_promocoes(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b'id="ver-promocoes"' in response.data
    assert b'href="/promocoes"' in response.data


def test_pagina_de_promocoes_responde_200(client):
    assert client.get("/promocoes").status_code == 200


def test_apenas_produtos_promocionais_aparecem(dados, client):
    response = client.get("/promocoes")

    for nome in dados.promocionais:
        assert nome.encode() in response.data
    for nome in dados.comuns:
        assert nome.encode() not in response.data


def test_pagina_nao_omite_promocionais(dados, client):
    response = client.get("/promocoes")

    assert response.text.count("Adicionar ao carrinho") == len(dados.promocionais)


def test_usuario_volta_ao_catalogo_completo(dados, client):
    promocoes = client.get("/promocoes")

    assert b'id="voltar-catalogo"' in promocoes.data
    assert b'href="/"' in promocoes.data

    catalogo = client.get("/")

    assert catalogo.status_code == 200
    for nome in dados.promocionais + dados.comuns:
        assert nome.encode() in catalogo.data


def test_pagina_avisa_quando_nao_ha_promocionais(dados, sem_promocoes, client):
    response = client.get("/promocoes")

    assert b"Nenhum produto promocional no momento." in response.data
    for nome in dados.comuns:
        assert nome.encode() not in response.data


def test_servico_lista_somente_promocionais(dados, session):
    nomes = [produto.name for produto in list_promotional_products(session)]

    assert sorted(nomes) == sorted(dados.promocionais)


def test_servico_ordena_por_nome(dados, session):
    nomes = [produto.name for produto in list_promotional_products(session)]

    assert nomes == sorted(dados.promocionais)


def test_servico_retorna_lista_vazia_sem_promocionais(sem_promocoes, session):
    assert list_promotional_products(session) == []


def test_api_lista_somente_promocionais(dados, client):
    response = client.get("/promocoes/api")

    assert response.status_code == 200
    payload = response.get_json()
    assert sorted(item["name"] for item in payload) == sorted(dados.promocionais)
    assert all(item["promotional"] is True for item in payload)


def test_api_devolve_lista_vazia_sem_promocionais(sem_promocoes, client):
    assert client.get("/promocoes/api").get_json() == []
