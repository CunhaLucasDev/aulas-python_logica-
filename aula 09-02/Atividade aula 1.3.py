# Objetivo: Peça ao usuário para digitar seu nome, idade e cidade
#natal. Use uma f-string para formatar e exibir uma mensagem
#com essas informações.Instruções:
#1 - Solicitar o Nome do Usuário:
#Use a função input() para pedir ao usuário que insira seu nome.

#2 - Solicitar a Idade do Usuário:
#Use a função input() para pedir ao usuário que insira sua idade.
#Converta a entrada do usuário de string para um número (int).

#3 - Solicitar a Cidade Natal do Usuário:
#Use a função input() para pedir ao usuário que insira sua cidade
#natal.

#4 - Formatar e Exibir a Mensagem com f-string:
#Use uma f-string para formatar a mensagem com as informações
#fornecidas pelo usuário e exiba a mensagem usando a função
## print().


nome=input("Qual é o seu nome ?")
idade=int(input("Qual é a sua idade ?"))
cidadenatal=input("Qual é a sua cidade natal e o estado?")
print(f"Olá, {nome}, Bem vindo a Infinity School !!!. Vimos que é de {cidadenatal} e tem {idade} anos.")
