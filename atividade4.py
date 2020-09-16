#(Desafio 1) Crie um dicionário vazio semana = {} e o complete com uma chave para
#cada dia da semana, tendo como seu valor uma lista com as aulas que você tem
#nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).

listaIOT = ("IoT","Arduino")
listaModDados = ("Modelagem de Dados")
listaLingProg = ("Linguagem de Programação","Python")
listaVazia1   = () 
listaDesen    = ("Desenvolvimento Front-End")
listaVazia2   = ()
listaVazia3   = ()

semana = {
    "segunda-feira" : listaIOT,
    "terça-feira"   : listaModDados,
    "quarta-feira"  : listaLingProg,
    "quinta-feira"  : listaVazia1,
    "sexta-feira"   : listaDesen,
    "sábado"        : listaVazia2,
    "domingo"       : listaVazia3
}
print("Lista de matérias:",semana)