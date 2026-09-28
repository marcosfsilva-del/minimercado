# Sinalização De Produto Esgotado

Produtos com estoque igual a zero continuam visíveis no catálogo e recebem o
estado "Esgotado" no cartão. O botão de adicionar ao carrinho permanece
desabilitado pelo template do catálogo.

A regra considera esgotado qualquer estoque menor ou igual a zero. Produtos com
estoque positivo não recebem o estado.
