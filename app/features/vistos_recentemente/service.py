
def registrar_visualizacao(historico, produto_id):
    novo_historico = [
        produto for produto in historico
        if produto != produto_id
    ]

    novo_historico.insert(0, produto_id)

    return novo_historico
