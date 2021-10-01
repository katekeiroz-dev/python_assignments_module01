#1 – O projeto HealthTrack está tomando forma e podemos pensar em algoritmos que possam ser reaproveitados
# quando estivermos implementando o front e o back do nosso sistema. Uma das funções mais procuradas por
# usuários de aplicativos de saúde é o de controle de calorias ingeridas em um dia. Por essa razão, você
# deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu
# naquele dia e depois possa informar o número de calorias de cada um dos alimentos. Como não estudamos
# listas nesse capítulo você não deve se preocupar em armazenar todas as calorias digitadas, mas deve
# exibir o total de calorias no final.

somaCaloria = 0

dia = int(input("Informe quantos alimentos você consumiu ao longo do dia: "))
print('Agora informa o número de calorias de cada um dos alimentos consumidos')

for x in range(dia):
    cal = int(input(f' Qual o número de calorias para {x+1}º alimento? '))
    somaCaloria = somaCaloria + cal

print(f'O total de calorias que você consumiu no dia é: {somaCaloria} cal')





