nota1=int(input("Qual foi sua nota do primeiro trimestre?"))
nota2=int(input("Qual foi sua nota do segundo trimestre?"))
nota3=int(input("Qual foi sua nota do terceiro trimestre?"))

media=(nota1+nota2+nota3)/3

if media >=6:
    print("Aprovado:")
elif media>=4 :
    print("Recuperação:")
else:   
    print("Reprovado:")

