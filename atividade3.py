#Crie um dicionário que tenha como chave os itens básicos de cadastro de uma
#pessoa id, nome, cpf, telefone, email. Para os valores, coloque dados fictícios de
#uma pessoa.
#A. Mostre para o usuário apenas os VALORES, não as chaves.
#B. Adicione mais elementos ao dicionário, como: endereço, sexo. Não esqueça
#de colocar os valores fictícios para as novas chaves.
#C. Mostre ao usuário todos os elementos (chave e valor).

dados = {
"ID"       : "62345",  
"nome"     : "Ana Maria",
"CPF"      : "0000111122",
"telefone" : "99136598",
"email"    : "ana.66609@hotmail.com"
}
#Imprimindo valores
for x in dados.values():
    print("Dados: ",x)

#Adicionando itens endereço e sexo ao dicionário
dados ["endereço"] = "Centro"
dados ["sexo"]     = "Feminino"

#Chaves e Valores ordenados
for x in dados:
    print(x +":",dados[x])


