from flask import session


class CarrinhoCleanerService:
    """Responsavel por gerenciar a limpeza dos itens do carrinho do usuario.

    O carrinho deste projeto nao e um objeto de dominio: ele vive na sessao
    do Flask (`session["cart"]`), como um dicionario {product_id: quantidade},
    exatamente como e criado e manipulado em `app/core/routes/web.py`.
    Por isso o servico opera diretamente sobre `flask.session`, em vez de
    depender de um `market_service` com metodos de carrinho (que nao existem
    em `app/core`).
    """

    CART_SESSION_KEY = "cart"

    def limpar(self) -> bool:
        """Esvazia o carrinho da sessao atual, sem remover a chave da sessao.

        Retorna True quando existia um carrinho na sessao (mesmo que ja
        estivesse vazio) e False quando o usuario ainda nem tinha uma
        sessao de carrinho iniciada.
        """
        cart = session.get(self.CART_SESSION_KEY)
        if cart is None:
            return False

        cart.clear()
        # Assim como em app/core/routes/web.py, a mutacao de um dict dentro
        # da sessao precisa ser sinalizada manualmente para ser persistida.
        session.modified = True
        return True


# Funcao utilitaria para manter compatibilidade com a chamada da rota.
def executar_limpeza() -> bool:
    cleaner = CarrinhoCleanerService()
    return cleaner.limpar()
