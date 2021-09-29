#Por isso, você deve desenvolver um script que solicite o PESO e a ALTURA de uma pessoa.
# A partir disso, o script deva calcular o IMC (PESO dividido pelo quadrado da ALTURA) e
# informar em quais das faixas a pessoa se encontra:

nome = input("Ola, qual seu nome? ")
p = float(input(f"Por favor, informe qual seu peso {nome}? "))
a = float(input("agora, informe qual sua altura? "))
imc = (p / (a * 2))

print(f'Seu IMC é de {imc:.1f}')

if imc <= 16.99:
    print("Sinto muito, mas você esta com Baixo peso Grau III")
elif imc <= 18.49:
    print("Sinto muito, mas você esta com Baixo peso Grau I")
elif imc <= 24.99:
    print("Muito bem , você está com o peso ideal :) ")
elif imc <= 29.99:
    print(" Sinto muito , você está com sobrepeso. ")
elif imc <= 34.99:
    print("Sinto muito , você está com Obesidade Grau I. ")
elif imc <= 39.99:
    print("Sinto muito , você está com Obesidade Grau II.  ")
else:
    print("Atenção ! Você está com Obesidade Grau III, é recomendado buscar ajuda de um especialista. ")





