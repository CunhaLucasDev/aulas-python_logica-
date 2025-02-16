#Faça um programa que peça um ano, e informe se ele é um ano bissexto.
#OBS: para ser bissexto, o ano deve ser divisivel por 4 e não pode ser divisivel por 100, exceto os divisiveis por 400.

ano=int(input("Informe um ano ?:"))

if (ano % 4==0 and ano % 100 !=0) or ano % 400 ==0 : 
    print("Ano é bissexto:" )
else :
    print("Ano não é bissexto:")
    

