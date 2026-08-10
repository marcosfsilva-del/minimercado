# Banco De 120 Issues

Este documento organiza 120 issues em 40 modulos independentes. Cada aluno pode assumir um modulo completo com 3 issues.

Regra pedagogica:

- cada modulo deve funcionar sozinho;
- cada aluno cria as 3 issues do seu modulo no GitHub;
- cada aluno trabalha em uma branch propria;
- cada aluno cria testes para as 3 entregas;
- cada aluno cria a propria CI da branch;
- nao alterar `app/core/*` sem justificativa e aprovacao.

Formato sugerido de branch:

```text
feature/<numero-issue>-<slug>
```

Exemplo:

```text
feature/42-product-search
```

## Modulo 01 - Pesquisa De Produtos

### Issue 001 - Campo De Busca No Catalogo

Implementar busca por nome do produto no catalogo.

Criterios de aceitacao:

- o usuario consegue digitar um termo de busca;
- produtos cujo nome contem o termo continuam visiveis;
- produtos que nao correspondem ao termo ficam ocultos;
- busca vazia mostra todos os produtos.

### Issue 002 - Busca Por Descricao

Expandir a busca para considerar tambem a descricao do produto.

Criterios de aceitacao:

- a busca encontra produtos pelo nome;
- a busca encontra produtos pela descricao;
- a busca nao diferencia maiusculas e minusculas.

### Issue 003 - Testes Da Pesquisa

Criar testes da feature de pesquisa.

Criterios de aceitacao:

- existe teste para busca por nome;
- existe teste para busca por descricao;
- existe teste para busca vazia;
- `python3 tasks.py test` passa.

## Modulo 02 - Categorias

### Issue 004 - Filtro Por Categoria

Implementar filtro de produtos por categoria.

Criterios de aceitacao:

- o catalogo exibe uma lista de categorias;
- selecionar uma categoria filtra os produtos;
- existe opcao para voltar a ver todas as categorias.

### Issue 005 - Contador Por Categoria

Exibir a quantidade de produtos em cada categoria.

Criterios de aceitacao:

- cada categoria mostra um contador;
- o contador considera os produtos cadastrados;
- categorias sem produto nao aparecem.

### Issue 006 - Testes De Categoria

Criar testes para filtro e contadores de categoria.

Criterios de aceitacao:

- existe teste para filtro por categoria;
- existe teste para opcao "todas";
- existe teste para contador;
- `python3 tasks.py test` passa.

## Modulo 03 - Ordenacao

### Issue 007 - Ordenar Por Nome

Adicionar ordenacao alfabetica no catalogo.

Criterios de aceitacao:

- existe controle de ordenacao por nome;
- produtos podem ser ordenados de A a Z;
- produtos podem ser ordenados de Z a A.

### Issue 008 - Ordenar Por Preco

Adicionar ordenacao por preco.

Criterios de aceitacao:

- produtos podem ser ordenados do menor preco para o maior;
- produtos podem ser ordenados do maior preco para o menor;
- a ordenacao funciona junto com a listagem base.

### Issue 009 - Testes De Ordenacao

Criar testes da ordenacao.

Criterios de aceitacao:

- existe teste para nome crescente;
- existe teste para nome decrescente;
- existe teste para preco crescente;
- existe teste para preco decrescente.

## Modulo 04 - Detalhes Do Produto

### Issue 010 - Pagina De Detalhes

Criar pagina de detalhes para cada produto.

Criterios de aceitacao:

- cada produto possui link para detalhes;
- a pagina exibe nome, descricao, categoria, preco e estoque;
- produto inexistente retorna pagina de erro amigavel.

### Issue 011 - Botao Adicionar Nos Detalhes

Permitir adicionar produto ao carrinho pela pagina de detalhes.

Criterios de aceitacao:

- a pagina de detalhes possui botao de adicionar;
- o botao adiciona o produto correto;
- usuario volta ou segue para o carrinho sem erro.

### Issue 012 - Testes Dos Detalhes

Criar testes da pagina de detalhes.

Criterios de aceitacao:

- teste cobre produto existente;
- teste cobre produto inexistente;
- teste cobre adicionar ao carrinho pelos detalhes.

## Modulo 05 - Produtos Promocionais

### Issue 013 - Filtro De Promocoes

Criar filtro para mostrar apenas produtos promocionais.

Criterios de aceitacao:

- existe acao "ver promocoes";
- apenas produtos promocionais aparecem;
- usuario consegue voltar ao catalogo completo.

### Issue 014 - Destaque Visual De Promocao

Melhorar o destaque visual de produtos promocionais.

Criterios de aceitacao:

- produto promocional possui destaque claro;
- produto nao promocional nao recebe destaque;
- o destaque nao quebra o layout mobile.

### Issue 015 - Testes De Promocoes

Criar testes para filtro e destaque promocional.

Criterios de aceitacao:

- teste cobre filtro de promocao;
- teste cobre produto com flag promocional;
- teste cobre produto sem flag promocional.

## Modulo 06 - Estoque Baixo

### Issue 016 - Sinalizar Estoque Baixo

Exibir aviso quando o produto estiver com estoque baixo.

Criterios de aceitacao:

- produtos com estoque igual ou menor que 5 exibem aviso;
- produtos acima do limite nao exibem aviso;
- o limite fica documentado na feature.

### Issue 017 - Filtro De Estoque Baixo

Criar filtro para listar apenas produtos com estoque baixo.

Criterios de aceitacao:

- existe acao para filtrar estoque baixo;
- somente produtos dentro do limite aparecem;
- busca sem resultado exibe mensagem amigavel.

### Issue 018 - Testes De Estoque Baixo

Criar testes da feature de estoque baixo.

Criterios de aceitacao:

- teste cobre produto abaixo do limite;
- teste cobre produto acima do limite;
- teste cobre filtro sem resultados.

## Modulo 07 - Produtos Esgotados

### Issue 019 - Sinalizar Produto Esgotado

Exibir estado de produto esgotado.

Criterios de aceitacao:

- estoque zero mostra texto "esgotado";
- botao de adicionar fica desabilitado;
- produto continua visivel no catalogo.

### Issue 020 - Filtro De Esgotados

Criar filtro para produtos esgotados.

Criterios de aceitacao:

- usuario consegue listar apenas esgotados;
- usuario consegue voltar ao catalogo completo;
- mensagem aparece quando nao ha esgotados.

### Issue 021 - Testes De Esgotados

Criar testes para produtos esgotados.

Criterios de aceitacao:

- teste cobre exibicao de esgotado;
- teste cobre botao desabilitado;
- teste cobre filtro de esgotados.

## Modulo 08 - Limite De Estoque No Carrinho

### Issue 022 - Bloquear Quantidade Acima Do Estoque

Impedir que o usuario coloque no carrinho quantidade maior que o estoque.

Criterios de aceitacao:

- quantidade maxima respeita o estoque;
- tentativa acima do estoque mostra aviso;
- o carrinho mantem quantidade valida.

### Issue 023 - Mensagem De Estoque Disponivel

Exibir estoque disponivel no item do carrinho.

Criterios de aceitacao:

- cada item mostra o estoque atual;
- a mensagem atualiza apos alterar quantidade;
- layout continua legivel em telas pequenas.

### Issue 024 - Testes De Limite De Estoque

Criar testes para limite de estoque no carrinho.

Criterios de aceitacao:

- teste cobre quantidade valida;
- teste cobre quantidade acima do estoque;
- teste cobre mensagem de estoque disponivel.

## Modulo 09 - Limpar Carrinho

### Issue 025 - Botao Limpar Carrinho

Adicionar acao para remover todos os itens do carrinho.

Criterios de aceitacao:

- botao aparece quando ha itens;
- clicar remove todos os itens;
- carrinho vazio mostra mensagem correta.

### Issue 026 - Confirmacao Para Limpar Carrinho

Adicionar confirmacao antes de limpar o carrinho.

Criterios de aceitacao:

- usuario precisa confirmar a limpeza;
- cancelar mantem os itens;
- confirmar remove todos os itens.

### Issue 027 - Testes De Limpeza Do Carrinho

Criar testes para limpar carrinho.

Criterios de aceitacao:

- teste cobre exibicao do botao;
- teste cobre cancelamento;
- teste cobre limpeza confirmada.

## Modulo 10 - Subtotal No Carrinho

### Issue 028 - Exibir Subtotal Por Item

Mostrar subtotal de cada item no carrinho.

Criterios de aceitacao:

- subtotal usa preco vezes quantidade;
- subtotal aparece em cada linha;
- valores usam formato monetario brasileiro.

### Issue 029 - Atualizar Subtotal Ao Alterar Quantidade

Recalcular subtotal quando a quantidade muda.

Criterios de aceitacao:

- alterar quantidade altera subtotal;
- total geral permanece coerente;
- nao ha necessidade de recarregar dados externos.

### Issue 030 - Testes De Subtotal

Criar testes para subtotal por item.

Criterios de aceitacao:

- teste cobre calculo inicial;
- teste cobre alteracao de quantidade;
- teste cobre formato monetario.

## Modulo 11 - Contador Do Carrinho

### Issue 031 - Contador No Menu

Exibir quantidade total de itens no menu do carrinho.

Criterios de aceitacao:

- contador aparece ao lado do link Carrinho;
- contador soma quantidades, nao apenas produtos diferentes;
- contador desaparece ou zera quando carrinho esta vazio.

### Issue 032 - Atualizacao Do Contador

Atualizar contador ao adicionar, remover ou alterar quantidade.

Criterios de aceitacao:

- adicionar item aumenta contador;
- remover item reduz contador;
- alterar quantidade atualiza contador.

### Issue 033 - Testes Do Contador

Criar testes para contador do carrinho.

Criterios de aceitacao:

- teste cobre carrinho vazio;
- teste cobre adicionar item;
- teste cobre remover item.

## Modulo 12 - Confirmacao De Remocao

### Issue 034 - Confirmar Remocao De Item

Adicionar confirmacao antes de remover item do carrinho.

Criterios de aceitacao:

- clicar em remover pede confirmacao;
- cancelar mantem o item;
- confirmar remove o item.

### Issue 035 - Mensagem Apos Remover Item

Exibir mensagem apos remocao de item.

Criterios de aceitacao:

- mensagem informa produto removido;
- mensagem aparece uma vez;
- carrinho reflete a remocao.

### Issue 036 - Testes De Remocao

Criar testes para confirmacao de remocao.

Criterios de aceitacao:

- teste cobre cancelamento;
- teste cobre confirmacao;
- teste cobre mensagem de sucesso.

## Modulo 13 - Cupom Simples

### Issue 037 - Campo De Cupom

Criar campo para informar cupom no carrinho.

Criterios de aceitacao:

- campo aparece no resumo do carrinho;
- usuario consegue enviar um codigo;
- cupom desconhecido mostra mensagem amigavel.

### Issue 038 - Cupom DEVOPS10

Implementar cupom `DEVOPS10` com 10% de desconto.

Criterios de aceitacao:

- cupom valido aplica 10% de desconto;
- total final exibe desconto;
- cupom invalido nao altera total.

### Issue 039 - Testes De Cupom

Criar testes para cupom simples.

Criterios de aceitacao:

- teste cobre cupom valido;
- teste cobre cupom invalido;
- teste cobre total com desconto.

## Modulo 14 - Desconto Por Categoria

### Issue 040 - Regra De Desconto Por Categoria

Criar regra de desconto para uma categoria especifica.

Criterios de aceitacao:

- uma categoria definida recebe desconto;
- outras categorias nao recebem desconto;
- regra fica documentada na feature.

### Issue 041 - Exibir Desconto Por Categoria

Mostrar desconto aplicado no resumo do carrinho.

Criterios de aceitacao:

- resumo exibe valor do desconto;
- resumo exibe total final;
- layout continua claro com ou sem desconto.

### Issue 042 - Testes De Desconto Por Categoria

Criar testes da regra de desconto por categoria.

Criterios de aceitacao:

- teste cobre categoria com desconto;
- teste cobre categoria sem desconto;
- teste cobre total final.

## Modulo 15 - Frete Gratis

### Issue 043 - Regra De Frete Gratis

Criar regra de frete gratis para compras acima de um valor minimo.

Criterios de aceitacao:

- valor minimo fica documentado;
- compras acima do valor exibem frete gratis;
- compras abaixo exibem mensagem de quanto falta.

### Issue 044 - Indicador De Progresso Para Frete

Exibir progresso ate atingir frete gratis.

Criterios de aceitacao:

- indicador aparece no carrinho;
- indicador chega a 100% quando atingir o minimo;
- indicador nao quebra layout mobile.

### Issue 045 - Testes De Frete Gratis

Criar testes da feature de frete gratis.

Criterios de aceitacao:

- teste cobre compra abaixo do minimo;
- teste cobre compra acima do minimo;
- teste cobre mensagem de valor restante.

## Modulo 16 - Leve 3 Pague 2

### Issue 046 - Regra Leve 3 Pague 2

Implementar promocao "leve 3 pague 2" para uma categoria ou produto.

Criterios de aceitacao:

- regra aplica desconto a cada grupo de 3;
- quantidade menor que 3 nao recebe desconto;
- produto/categoria da regra fica documentado.

### Issue 047 - Exibir Economia Da Promocao

Mostrar economia gerada pela promocao.

Criterios de aceitacao:

- carrinho mostra valor economizado;
- total final considera economia;
- mensagem aparece apenas quando regra se aplica.

### Issue 048 - Testes Leve 3 Pague 2

Criar testes da promocao.

Criterios de aceitacao:

- teste cobre 2 itens sem desconto;
- teste cobre 3 itens com desconto;
- teste cobre 6 itens com dois descontos.

## Modulo 17 - Compra Minima

### Issue 049 - Bloquear Checkout Abaixo Do Minimo

Definir valor minimo para finalizar compra.

Criterios de aceitacao:

- checkout fica bloqueado abaixo do minimo;
- usuario ve quanto falta para atingir o minimo;
- compras acima do minimo podem finalizar.

### Issue 050 - Mensagem De Compra Minima

Exibir mensagem clara no carrinho e checkout.

Criterios de aceitacao:

- carrinho mostra regra de compra minima;
- checkout mostra bloqueio quando necessario;
- mensagem desaparece quando total e suficiente.

### Issue 051 - Testes De Compra Minima

Criar testes da regra de compra minima.

Criterios de aceitacao:

- teste cobre total abaixo do minimo;
- teste cobre total igual ao minimo;
- teste cobre total acima do minimo.

## Modulo 18 - Nome Do Cliente

### Issue 052 - Nome Obrigatorio No Checkout

Tornar nome do cliente obrigatorio no checkout.

Criterios de aceitacao:

- checkout exige nome;
- nome vazio mostra erro;
- pedido salvo contem nome informado.

### Issue 053 - Validacao De Tamanho Do Nome

Validar tamanho minimo e maximo do nome.

Criterios de aceitacao:

- nome curto demais mostra erro;
- nome longo demais mostra erro;
- nome valido permite finalizar.

### Issue 054 - Testes De Nome Do Cliente

Criar testes para validacao de nome.

Criterios de aceitacao:

- teste cobre nome vazio;
- teste cobre nome invalido;
- teste cobre nome valido.

## Modulo 19 - CPF Do Cliente

### Issue 055 - Campo CPF No Checkout

Adicionar campo de CPF no checkout.

Criterios de aceitacao:

- checkout exibe campo CPF;
- CPF e salvo junto ao pedido ou cliente;
- campo aceita CPF com ou sem pontuacao.

### Issue 056 - Validacao Simples De CPF

Criar validacao simples de formato do CPF.

Criterios de aceitacao:

- CPF com 11 digitos e aceito;
- CPF com tamanho invalido e rejeitado;
- mensagem de erro e clara.

### Issue 057 - Testes De CPF

Criar testes para campo e validacao de CPF.

Criterios de aceitacao:

- teste cobre CPF valido;
- teste cobre CPF invalido;
- teste cobre persistencia do CPF.

## Modulo 20 - Forma De Pagamento

### Issue 058 - Selecionar Forma De Pagamento

Adicionar selecao de forma de pagamento no checkout.

Criterios de aceitacao:

- opcoes incluem dinheiro, pix e cartao;
- usuario precisa selecionar uma opcao;
- pedido registra a forma escolhida.

### Issue 059 - Resumo Da Forma De Pagamento

Exibir forma de pagamento no resumo do pedido.

Criterios de aceitacao:

- pedidos mostram a forma selecionada;
- API retorna forma de pagamento;
- valor aparece de forma legivel.

### Issue 060 - Testes De Pagamento

Criar testes para forma de pagamento.

Criterios de aceitacao:

- teste cobre opcao obrigatoria;
- teste cobre pedido com pix;
- teste cobre exibicao no historico.

## Modulo 21 - Forma De Entrega

### Issue 061 - Selecionar Forma De Entrega

Adicionar retirada ou entrega no checkout.

Criterios de aceitacao:

- usuario escolhe retirada ou entrega;
- pedido registra a escolha;
- retirada nao exige endereco.

### Issue 062 - Endereco Para Entrega

Exigir endereco quando forma for entrega.

Criterios de aceitacao:

- entrega exige endereco;
- retirada nao exige endereco;
- pedido de entrega salva endereco.

### Issue 063 - Testes De Entrega

Criar testes para forma de entrega.

Criterios de aceitacao:

- teste cobre retirada;
- teste cobre entrega sem endereco;
- teste cobre entrega com endereco.

## Modulo 22 - Codigo Do Pedido

### Issue 064 - Gerar Codigo Publico Do Pedido

Gerar codigo publico para cada pedido.

Criterios de aceitacao:

- cada pedido possui codigo legivel;
- codigo e diferente do id interno ou formatado;
- codigo aparece apos finalizar compra.

### Issue 065 - Buscar Pedido Por Codigo

Criar busca de pedido pelo codigo publico.

Criterios de aceitacao:

- usuario informa codigo;
- pedido encontrado e exibido;
- codigo inexistente mostra mensagem amigavel.

### Issue 066 - Testes De Codigo Do Pedido

Criar testes para codigo de pedido.

Criterios de aceitacao:

- teste cobre geracao do codigo;
- teste cobre busca existente;
- teste cobre busca inexistente.

## Modulo 23 - Tela De Sucesso

### Issue 067 - Criar Tela De Sucesso

Criar tela especifica apos finalizar compra.

Criterios de aceitacao:

- usuario e redirecionado apos compra;
- tela mostra numero ou codigo do pedido;
- tela mostra total da compra.

### Issue 068 - Acoes Na Tela De Sucesso

Adicionar acoes para voltar ao catalogo e ver pedidos.

Criterios de aceitacao:

- existe acao para voltar ao catalogo;
- existe acao para ver historico de pedidos;
- acoes funcionam corretamente.

### Issue 069 - Testes Da Tela De Sucesso

Criar testes para tela de sucesso.

Criterios de aceitacao:

- teste cobre redirecionamento;
- teste cobre exibicao do pedido;
- teste cobre links de acao.

## Modulo 24 - Historico De Pedidos

### Issue 070 - Filtro No Historico

Adicionar filtro por nome do cliente no historico de pedidos.

Criterios de aceitacao:

- usuario filtra por nome;
- filtro nao diferencia maiusculas e minusculas;
- sem termo mostra todos os pedidos.

### Issue 071 - Ordenacao Do Historico

Adicionar ordenacao por data e total.

Criterios de aceitacao:

- usuario ordena por data;
- usuario ordena por total;
- ordenacao funciona com filtro aplicado.

### Issue 072 - Testes Do Historico

Criar testes para historico de pedidos.

Criterios de aceitacao:

- teste cobre filtro por cliente;
- teste cobre ordenacao por data;
- teste cobre ordenacao por total.

## Modulo 25 - Repetir Compra

### Issue 073 - Botao Repetir Compra

Adicionar botao para repetir um pedido anterior.

Criterios de aceitacao:

- pedido no historico possui acao repetir;
- itens do pedido sao adicionados ao carrinho;
- quantidades sao preservadas quando ha estoque.

### Issue 074 - Tratar Falta De Estoque Ao Repetir

Tratar produtos sem estoque suficiente ao repetir compra.

Criterios de aceitacao:

- item sem estoque nao quebra a repeticao;
- usuario recebe aviso;
- itens disponiveis continuam no carrinho.

### Issue 075 - Testes De Repetir Compra

Criar testes para repetir compra.

Criterios de aceitacao:

- teste cobre repeticao com estoque;
- teste cobre repeticao sem estoque;
- teste cobre carrinho resultante.

## Modulo 26 - Baixa Automatica De Estoque

### Issue 076 - Confirmar Baixa No Checkout

Garantir baixa de estoque ao finalizar compra.

Criterios de aceitacao:

- estoque diminui conforme quantidade comprada;
- pedido registra itens comprados;
- estoque nao muda se checkout falhar.

### Issue 077 - Exibir Estoque Atual Apos Compra

Atualizar catalogo com estoque reduzido apos compra.

Criterios de aceitacao:

- catalogo mostra estoque novo;
- produto pode ficar esgotado;
- usuario nao ve estoque antigo apos finalizar.

### Issue 078 - Testes De Baixa De Estoque

Criar testes para baixa automatica.

Criterios de aceitacao:

- teste cobre baixa bem sucedida;
- teste cobre falha sem baixa;
- teste cobre catalogo apos compra.

## Modulo 27 - Bloqueio De Estoque Negativo

### Issue 079 - Bloquear Estoque Negativo

Impedir que qualquer fluxo gere estoque negativo.

Criterios de aceitacao:

- compra acima do estoque e rejeitada;
- estoque nunca fica menor que zero;
- mensagem informa o problema.

### Issue 080 - Validacao Na API

Adicionar validacao de estoque na criacao de pedido via API.

Criterios de aceitacao:

- API rejeita quantidade acima do estoque;
- API retorna status adequado;
- resposta contem mensagem clara.

### Issue 081 - Testes De Estoque Negativo

Criar testes contra estoque negativo.

Criterios de aceitacao:

- teste cobre checkout web;
- teste cobre endpoint API;
- teste cobre estoque preservado.

## Modulo 28 - Reposicao De Estoque

### Issue 082 - Tela De Reposicao

Criar tela simples para repor estoque de produto.

Criterios de aceitacao:

- usuario seleciona produto;
- usuario informa quantidade;
- estoque aumenta apos confirmar.

### Issue 083 - Registrar Movimento De Reposicao

Registrar movimentacao de estoque para reposicoes.

Criterios de aceitacao:

- reposicao cria movimento do tipo reposicao;
- movimento registra produto e quantidade;
- dados aparecem em consulta interna ou pagina da feature.

### Issue 084 - Testes De Reposicao

Criar testes para reposicao de estoque.

Criterios de aceitacao:

- teste cobre aumento de estoque;
- teste cobre quantidade invalida;
- teste cobre movimento registrado.

## Modulo 29 - Movimentacoes De Estoque

### Issue 085 - Listar Movimentacoes

Criar pagina para listar movimentacoes de estoque.

Criterios de aceitacao:

- pagina lista produto, tipo, quantidade e data;
- movimentacoes aparecem em ordem recente;
- pagina lida com lista vazia.

### Issue 086 - Filtrar Movimentacoes Por Produto

Adicionar filtro por produto na lista de movimentacoes.

Criterios de aceitacao:

- usuario seleciona ou busca produto;
- lista exibe apenas movimentos do produto;
- filtro vazio mostra todos.

### Issue 087 - Testes De Movimentacoes

Criar testes para movimentacoes.

Criterios de aceitacao:

- teste cobre lista;
- teste cobre filtro;
- teste cobre estado vazio.

## Modulo 30 - Favoritos

### Issue 088 - Marcar Produto Como Favorito

Permitir marcar produto como favorito.

Criterios de aceitacao:

- produto possui acao favoritar;
- favorito fica salvo na sessao ou tabela da feature;
- usuario visualiza estado favoritado.

### Issue 089 - Filtro De Favoritos

Criar tela ou filtro para produtos favoritos.

Criterios de aceitacao:

- usuario consegue ver favoritos;
- usuario consegue remover favorito;
- lista vazia mostra mensagem amigavel.

### Issue 090 - Testes De Favoritos

Criar testes para favoritos.

Criterios de aceitacao:

- teste cobre favoritar;
- teste cobre desfavoritar;
- teste cobre lista de favoritos.

## Modulo 31 - Vistos Recentemente

### Issue 091 - Registrar Produto Visto

Registrar produtos acessados recentemente.

Criterios de aceitacao:

- acessar detalhes registra produto;
- lista preserva ordem do mais recente;
- produtos repetidos nao duplicam.

### Issue 092 - Exibir Vistos Recentemente

Exibir lista de vistos recentemente.

Criterios de aceitacao:

- lista aparece no catalogo ou pagina propria;
- lista possui limite documentado;
- item da lista leva ao produto.

### Issue 093 - Testes De Vistos Recentemente

Criar testes para vistos recentemente.

Criterios de aceitacao:

- teste cobre registro;
- teste cobre ordem;
- teste cobre remocao de duplicados.

## Modulo 32 - Total Gasto Por Cliente

### Issue 094 - Calcular Total Gasto

Calcular total gasto por cliente com base nos pedidos.

Criterios de aceitacao:

- cliente com pedidos mostra soma correta;
- cliente sem pedidos mostra zero;
- calculo considera total dos pedidos.

### Issue 095 - Exibir Ranking De Clientes

Criar pagina de ranking por total gasto.

Criterios de aceitacao:

- ranking mostra cliente e total;
- ranking ordena do maior para o menor;
- lista vazia mostra mensagem amigavel.

### Issue 096 - Testes De Total Gasto

Criar testes para total gasto por cliente.

Criterios de aceitacao:

- teste cobre cliente com um pedido;
- teste cobre cliente com varios pedidos;
- teste cobre ranking.

## Modulo 33 - Ultima Compra Do Cliente

### Issue 097 - Identificar Ultima Compra

Identificar a ultima compra de cada cliente.

Criterios de aceitacao:

- cliente com pedidos mostra data da ultima compra;
- cliente sem pedidos mostra estado vazio;
- regra usa pedido mais recente.

### Issue 098 - Exibir Ultima Compra No Historico

Exibir ultima compra em uma pagina ou bloco da feature.

Criterios de aceitacao:

- mostra nome do cliente;
- mostra data e total da ultima compra;
- permite acessar o pedido relacionado.

### Issue 099 - Testes De Ultima Compra

Criar testes para ultima compra.

Criterios de aceitacao:

- teste cobre cliente sem pedidos;
- teste cobre cliente com pedidos;
- teste cobre pedido mais recente.

## Modulo 34 - Health Check Avancado

### Issue 100 - Endpoint De Health Detalhado

Criar endpoint de health detalhado da feature.

Criterios de aceitacao:

- endpoint retorna status da aplicacao;
- endpoint retorna versao;
- endpoint retorna horario da resposta.

### Issue 101 - Health Do Banco

Adicionar verificacao simples de banco no health detalhado.

Criterios de aceitacao:

- endpoint verifica conexao com SQLite;
- resposta indica banco ok ou falha;
- falha retorna status adequado.

### Issue 102 - Testes De Health Avancado

Criar testes do health detalhado.

Criterios de aceitacao:

- teste cobre status ok;
- teste cobre informacoes de versao;
- teste cobre verificacao de banco.

## Modulo 35 - Readiness

### Issue 103 - Endpoint Readiness

Criar endpoint de readiness especifico.

Criterios de aceitacao:

- endpoint retorna ready quando aplicacao pode receber trafego;
- endpoint usa formato JSON;
- endpoint fica documentado no README da feature.

### Issue 104 - Readiness Com Banco

Readiness deve considerar acesso ao banco.

Criterios de aceitacao:

- banco acessivel retorna ready;
- banco indisponivel retorna not ready;
- status HTTP reflete o estado.

### Issue 105 - Testes De Readiness

Criar testes para readiness.

Criterios de aceitacao:

- teste cobre readiness ok;
- teste cobre resposta JSON;
- teste cobre verificacao de banco.

## Modulo 36 - Versionamento Da Aplicacao

### Issue 106 - Endpoint De Versao

Criar endpoint para retornar versao da aplicacao.

Criterios de aceitacao:

- endpoint retorna `APP_VERSION`;
- endpoint retorna `COMMIT_SHA`;
- endpoint usa JSON.

### Issue 107 - Exibir Versao No Rodape

Exibir versao da aplicacao no frontend.

Criterios de aceitacao:

- rodape mostra versao;
- commit aparece quando configurado;
- ausencia de variavel usa valor local.

### Issue 108 - Testes De Versao

Criar testes para versionamento.

Criterios de aceitacao:

- teste cobre endpoint;
- teste cobre valor padrao;
- teste cobre exibicao no frontend.

## Modulo 37 - Request ID

### Issue 109 - Gerar Request ID

Gerar identificador unico para cada requisicao.

Criterios de aceitacao:

- cada request recebe id;
- id aparece no header de resposta;
- id pode ser reutilizado se cliente enviar header.

### Issue 110 - Exibir Request ID Em Erros

Incluir request id em respostas de erro.

Criterios de aceitacao:

- erro web mostra codigo de rastreio;
- erro API retorna request id no JSON;
- logs incluem request id.

### Issue 111 - Testes De Request ID

Criar testes para request id.

Criterios de aceitacao:

- teste cobre geracao automatica;
- teste cobre header enviado pelo cliente;
- teste cobre resposta de erro.

## Modulo 38 - Metricas Simples

### Issue 112 - Contador De Requisicoes

Criar metrica simples de quantidade de requisicoes.

Criterios de aceitacao:

- contador aumenta a cada requisicao;
- endpoint de metricas retorna contador;
- formato e documentado.

### Issue 113 - Metricas Por Rota

Adicionar contagem por rota.

Criterios de aceitacao:

- metricas mostram rota;
- metricas mostram quantidade por rota;
- rotas desconhecidas nao quebram metricas.

### Issue 114 - Testes De Metricas

Criar testes para metricas.

Criterios de aceitacao:

- teste cobre contador geral;
- teste cobre contador por rota;
- teste cobre endpoint de metricas.

## Modulo 39 - Logs De Auditoria

### Issue 115 - Registrar Evento De Pedido

Criar log de auditoria ao finalizar pedido.

Criterios de aceitacao:

- pedido criado gera evento;
- evento contem tipo, data e id do pedido;
- evento pode ser consultado.

### Issue 116 - Registrar Evento De Carrinho

Criar log de auditoria para acoes importantes do carrinho.

Criterios de aceitacao:

- adicionar produto gera evento;
- remover produto gera evento;
- limpar carrinho gera evento quando existir.

### Issue 117 - Testes De Auditoria

Criar testes para logs de auditoria.

Criterios de aceitacao:

- teste cobre evento de pedido;
- teste cobre evento de carrinho;
- teste cobre consulta de eventos.

## Modulo 40 - Acessibilidade E UX Basica

### Issue 118 - Melhorar Labels De Formularios

Revisar formularios para garantir labels claros.

Criterios de aceitacao:

- inputs possuem label associado;
- botoes possuem texto claro;
- mensagens de erro ficam proximas ao campo.

### Issue 119 - Estados Vazios Amigaveis

Melhorar estados vazios do catalogo, carrinho e pedidos.

Criterios de aceitacao:

- carrinho vazio tem mensagem e acao;
- pedidos vazios tem mensagem clara;
- filtros sem resultado orientam o usuario.

### Issue 120 - Testes De UX Basica

Criar testes para labels e estados vazios.

Criterios de aceitacao:

- teste cobre label de formulario;
- teste cobre carrinho vazio;
- teste cobre lista vazia de pedidos.
