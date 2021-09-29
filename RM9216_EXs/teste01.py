# saber se o numero é par ou impar

n = int(input('Digite um numero: '))
if n % 2 ==0:
    print(f'O número {n} é par')

else:
    print(f'O número {n} é impar')


# saber idade


nome = input('Qual seu nome? ')
anoNas = int(input('qual seu ano de nascimento? '))

idade = 2021 - anoNas

print(f'Ola {nome}, você tem {idade} anos')