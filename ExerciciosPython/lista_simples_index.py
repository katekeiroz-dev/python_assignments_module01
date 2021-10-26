# Script index


from lista_simples_funcoes import *

# Menu de opções dos bairros disponíveis ao usuário
print('Bairros disponíveis: \n1 - Bela Vista \n2 - Bom Retiro\n3 - Cambucí\n4 - Consolação\n5 - Liberdade\n6 - República\n7 - Santa Cecília\n')

# Variável responsável por frear o while.
x = -1

while x != 8:

    bairro = int(input('Digite o número do bairro: '))
    if bairro == 1:
        recomendar_b1()
        x = 8
    elif bairro == 2:
        recomendar_b2()
        x = 8
    elif bairro == 3:
        recomendar_b3()
        x = 8
    elif bairro == 4:
        recomendar_b4()
        x = 8
    elif bairro == 5:
        recomendar_b5()
        x = 8
    elif bairro == 6:
        recomendar_b6()
        x = 8
    elif bairro == 7:
        recomendar_b7()
        x = 8
    else:
        bairro > 8
        print('Bairro não cadastrado. \nTente novamente')