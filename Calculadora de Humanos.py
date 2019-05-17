print("instalador Funcionando!")
input("Pressione ENTER para continuar")

print("Vamos ver seu IMC e há quanto tempo você está vivo em dias, minutos e segundos.")
nome = input("Nome: ")
sobrenome = input ("Sobrenome: ")
input ("Dia e Mês de Nascimento: ")
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)
idade = int(input("Idade: "))
dias = idade * 365
minutos = idade * 525948     
segundos = idade * 31556926
print(nome,sobrenome,'Seu IMC é {}'.format(imc), "Já viveu por", dias,"Dias", minutos, "Minutos e", segundos, "Segundos!  Aproveite o Resto de sua vida!")

input ("Aperte Enter Para Finalizar")
print ("fim")
