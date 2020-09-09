#Crie uma tupla com 5 itens, após, tente alterar o valor de um item. Observe o que
#acontece ao executar o código. Coloque um comentário no seu código explicando
#o que aconteceu.

minhaTupla = ("Azul","Amarelo","Vermelho","Laranja","Verde")
print("Tupla de cores:", type(minhaTupla))

minhaTupla["azul"] = "roxo"
print("Tupla modificada:", minhaTupla)
#Acontece um erro ao tentar alterar algo dentro da tupla dessa forma, pois a classe tuple é
#imutável, impossibilitando qualque mudança. 