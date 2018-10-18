# lendo dados do teclado


nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)  # ou altura ** 2
print(f"{nome}, seu imc é: {imc:.2f}")