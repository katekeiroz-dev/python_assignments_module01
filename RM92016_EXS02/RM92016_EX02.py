#2 – Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças
#aprendam a controlar os seus gastos.
#Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar
# QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e,
# na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.
#Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.





print('___________________________________________')
transicaoDia = int(input('Transação ao longo do dia'))
print('Agora informa o valor de cada transação: ')
soma = 0

for x in range(transicaoDia):
    valor = float(input(f' Qual o valor da {x+1}º transação? '))
    soma = soma + valor
    media = soma / transicaoDia

print('_______________________________________')
print(f'TOTAL GASTOS NO DIA : R$ {soma:.2f} ')
print(f'MÉDIA : R$ {media:.2f} ')

