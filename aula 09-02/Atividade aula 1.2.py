#Objetivo: Faça um programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha
#20 dias no mês).

SalarioMensal = float(input("Informe seu salario mensal?:" ))
HorasTrabalhadasSemana = int(input("Informe quantas horas de trabalho por semana ?:"))

print(HorasTrabalhadasSemana*4)
TotalDeHorasporMes = HorasTrabalhadasSemana*4

Resultado= (SalarioMensal/TotalDeHorasporMes)

print(f"O seu Salario por hora é de {Resultado}:")


                       