from lista_simples_bd import *

# Função de inclusão de novo restaurante para lista original, os dados serão adicionados ao final da lista
def add_b1():
    nome = input('Nome restaurante: ')
    rank = float(input('Digite o ranking: '))
    dista = float(input('Distancia: '))
    rest_b1.append(nome)
    ranking_b1.append(rank)
    dist_b1.append(dista)
    # Verificador de banco de dados após inclusão de novo restaurante
    for n in range(len(rest_b1)):
        print("=" * 30)
        print('\n')
        print(f'{rest_b1[n]}, {ranking_b1[n]}, {dist_b1[n]}')
        print("=" * 30)
        print('\n')

def add_b2():
    nome = input('Nome restaurante: ')
    rank = float(input('Digite o ranking: '))
    dista = float(input('Distancia: '))
    rest_b2.append(nome)
    ranking_b2.append(rank)
    dist_b2.append(dista)
    # Verificador de banco de dados após inclusão de novo restaurante
    for n in range(len(rest_b2)):
        print("=" * 30)
        print('\n')
        print(f'{rest_b2[n]}, {ranking_b2[n]}, {dist_b2[n]}')
        print("=" * 30)
        print('\n')

def add_b3():
    nome = input('Nome restaurante: ')
    rank = float(input('Digite o ranking: '))
    dista = float(input('Distancia: '))
    rest_b3.append(nome)
    ranking_b3.append(rank)
    dist_b3.append(dista)
    # Verificador de banco de dados após inclusão de novo restaurante
    for n in range(len(rest_b3)):
        print("=" * 30)
        print('\n')
        print(f'{rest_b3[n]}, {ranking_b3[n]}, {dist_b3[n]}')
        print("=" * 30)
        print('\n')

def add_b4():
    nome = input('Nome restaurante: ')
    rank = float(input('Digite o ranking: '))
    dista = float(input('Distancia: '))
    rest_b4.append(nome)
    ranking_b4.append(rank)
    dist_b4.append(dista)
    # Verificador de banco de dados após inclusão de novo restaurante
    for n in range(len(rest_b4)):
        print("=" * 30)
        print('\n')
        print(f'{rest_b4[n]}, {ranking_b4[n]}, {dist_b4[n]}')
        print("=" * 30)
        print('\n')

def add_b5():
    nome = input('Nome restaurante: ')
    rank = float(input('Digite o ranking: '))
    dista = float(input('Distancia: '))
    rest_b5.append(nome)
    ranking_b5.append(rank)
    dist_b5.append(dista)
    # Verificador de banco de dados após inclusão de novo restaurante
    for n in range(len(rest_b5)):
        print("=" * 30)
        print('\n')
        print(f'{rest_b5[n]}, {ranking_b5[n]}, {dist_b5[n]}')
        print("=" * 30)
        print('\n')

def add_b6():
    nome = input('Nome restaurante: ')
    rank = float(input('Digite o ranking: '))
    dista = float(input('Distancia: '))
    rest_b6.append(nome)
    ranking_b6.append(rank)
    dist_b6.append(dista)
    # Verificador de banco de dados após inclusão de novo restaurante
    for n in range(len(rest_b6)):
        print("=" * 30)
        print('\n')
        print(f'{rest_b6[n]}, {ranking_b6[n]}, {dist_b6[n]}')
        print("=" * 30)
        print('\n')

def add_b7():
    nome = input('Nome restaurante: ')
    rank = float(input('Digite o ranking: '))
    dista = float(input('Distancia: '))
    rest_b7.append(nome)
    ranking_b7.append(rank)
    dist_b7.append(dista)
    # Verificador de banco de dados após inclusão de novo restaurante
    for n in range(len(rest_b7)):
        print("=" * 30)
        print('\n')
        print(f'{rest_b7[n]}, {ranking_b7[n]}, {dist_b7[n]}')
        print("=" * 30)
        print('\n')


# Função para criar ranking de restaurantes recomendados sem alterar listas originais, na sequencia (nome do restaurante, ranking, distancia)
def recomendar_b1 ():

    # Listas vazias que serão usadas na ordenação do ranking e exibição no output final
    rest_novo = []
    ranking_novo = []
    dist_novo = []

    # Comando para criação da nova lista que gera a saída de dados ordenadamente
    for n in rest_b1:
        rest_novo.append(n)

    for n in ranking_b1:
        ranking_novo.append(n)

    for n in dist_b1:
        dist_novo.append(n)

    # Algoritimo que valida ranking e distancia, em caso de empate nos rankings
    for n in range(len(rest_b1)):
        for x in range(n+1,len(rest_b1)):

            # Critério de desempate por distância entre restaurantes com o mesmo ranking
            if ranking_novo[n] == ranking_novo[x]:
                if dist_novo[n] > dist_novo[x]:

                    temp_1 = rest_novo[n]
                    rest_novo[n] = rest_novo[x]
                    rest_novo[x] = temp_1

                    temp_2 = ranking_novo[n]
                    ranking_novo[n] = ranking_novo[x]
                    ranking_novo[x] = temp_2

                    temp_3 = dist_novo[n]
                    dist_novo[n] = dist_novo[x]
                    dist_novo[x] = temp_3

            # Verificador do ranking do restaurante e ordenação da sequência de recomendações
            elif ranking_novo[n] < ranking_novo[x]:

                temp1 = rest_novo[n]
                rest_novo[n] = rest_novo[x]
                rest_novo[x] = temp1

                temp2 = ranking_novo[n]
                ranking_novo[n] = ranking_novo[x]
                ranking_novo[x] = temp2

                temp3 = dist_novo[n]
                dist_novo[n] = dist_novo[x]
                dist_novo[x] = temp3
    # Apresentação dos resultados da recomendação
    print('\n+++++     Recomendações     +++++\n')
    linha = ('='*30)
    for n in range(len(rest_b1)):
        print(f'Restaurante: {rest_novo[n]}\nNota: {ranking_novo[n]}\nDistância {dist_novo[n]}\n')
        print(linha)

def recomendar_b2 ():

    # Listas vazias que serão usadas na ordenação do ranking e exibição no output final
    rest_novo = []
    ranking_novo = []
    dist_novo = []

    # Comando para criação da nova lista que gera a saída de dados ordenadamente
    for n in rest_b2:
        rest_novo.append(n)

    for n in ranking_b2:
        ranking_novo.append(n)

    for n in dist_b2:
        dist_novo.append(n)

    # Algoritimo que valida ranking e distancia, em caso de empate nos rankings
    for n in range(len(rest_b2)):
        for x in range(n+1,len(rest_b2)):

            # Critério de desempate por distância entre restaurantes com o mesmo ranking
            if ranking_novo[n] == ranking_novo[x]:
                if dist_novo[n] > dist_novo[x]:

                    temp_1 = rest_novo[n]
                    rest_novo[n] = rest_novo[x]
                    rest_novo[x] = temp_1

                    temp_2 = ranking_novo[n]
                    ranking_novo[n] = ranking_novo[x]
                    ranking_novo[x] = temp_2

                    temp_3 = dist_novo[n]
                    dist_novo[n] = dist_novo[x]
                    dist_novo[x] = temp_3

            # Verificador do ranking do restaurante e ordenação da sequência de recomendações
            elif ranking_novo[n] < ranking_novo[x]:

                temp1 = rest_novo[n]
                rest_novo[n] = rest_novo[x]
                rest_novo[x] = temp1

                temp2 = ranking_novo[n]
                ranking_novo[n] = ranking_novo[x]
                ranking_novo[x] = temp2

                temp3 = dist_novo[n]
                dist_novo[n] = dist_novo[x]
                dist_novo[x] = temp3
    # Apresentação dos resultados da recomendação
    print('\n+++++     Recomendações     +++++\n')
    linha = ('='*30)
    for n in range(len(rest_b2)):
        print(f'Restaurante: {rest_novo[n]}\nNota: {ranking_novo[n]}\nDistância {dist_novo[n]}\n')
        print(linha)

def recomendar_b3 ():

    # Listas vazias que serão usadas na ordenação do ranking e exibição no output final
    rest_novo = []
    ranking_novo = []
    dist_novo = []

    # Comando para criação da nova lista que gera a saída de dados ordenadamente
    for n in rest_b3:
        rest_novo.append(n)

    for n in ranking_b3:
        ranking_novo.append(n)

    for n in dist_b3:
        dist_novo.append(n)

    # Algoritimo que valida ranking e distancia, em caso de empate nos rankings
    for n in range(len(rest_b3)):
        for x in range(n+1,len(rest_b3)):

            # Critério de desempate por distância entre restaurantes com o mesmo ranking
            if ranking_novo[n] == ranking_novo[x]:
                if dist_novo[n] > dist_novo[x]:

                    temp_1 = rest_novo[n]
                    rest_novo[n] = rest_novo[x]
                    rest_novo[x] = temp_1

                    temp_2 = ranking_novo[n]
                    ranking_novo[n] = ranking_novo[x]
                    ranking_novo[x] = temp_2

                    temp_3 = dist_novo[n]
                    dist_novo[n] = dist_novo[x]
                    dist_novo[x] = temp_3

            # Verificador do ranking do restaurante e ordenação da sequência de recomendações
            elif ranking_novo[n] < ranking_novo[x]:

                temp1 = rest_novo[n]
                rest_novo[n] = rest_novo[x]
                rest_novo[x] = temp1

                temp2 = ranking_novo[n]
                ranking_novo[n] = ranking_novo[x]
                ranking_novo[x] = temp2

                temp3 = dist_novo[n]
                dist_novo[n] = dist_novo[x]
                dist_novo[x] = temp3
    # Apresentação dos resultados da recomendação
    print('\n+++++     Recomendações     +++++\n')
    linha = ('='*30)
    for n in range(len(rest_b3)):
        print(f'Restaurante: {rest_novo[n]}\nNota: {ranking_novo[n]}\nDistância {dist_novo[n]}\n')
        print(linha)

def recomendar_b4 ():

    # Listas vazias que serão usadas na ordenação do ranking e exibição no output final
    rest_novo = []
    ranking_novo = []
    dist_novo = []

    # Comando para criação da nova lista que gera a saída de dados ordenadamente
    for n in rest_b4:
        rest_novo.append(n)

    for n in ranking_b4:
        ranking_novo.append(n)

    for n in dist_b4:
        dist_novo.append(n)

    # Algoritimo que valida ranking e distancia, em caso de empate nos rankings
    for n in range(len(rest_b4)):
        for x in range(n+1,len(rest_b4)):

            # Critério de desempate por distância entre restaurantes com o mesmo ranking
            if ranking_novo[n] == ranking_novo[x]:
                if dist_novo[n] > dist_novo[x]:

                    temp_1 = rest_novo[n]
                    rest_novo[n] = rest_novo[x]
                    rest_novo[x] = temp_1

                    temp_2 = ranking_novo[n]
                    ranking_novo[n] = ranking_novo[x]
                    ranking_novo[x] = temp_2

                    temp_3 = dist_novo[n]
                    dist_novo[n] = dist_novo[x]
                    dist_novo[x] = temp_3

            # Verificador do ranking do restaurante e ordenação da sequência de recomendações
            elif ranking_novo[n] < ranking_novo[x]:

                temp1 = rest_novo[n]
                rest_novo[n] = rest_novo[x]
                rest_novo[x] = temp1

                temp2 = ranking_novo[n]
                ranking_novo[n] = ranking_novo[x]
                ranking_novo[x] = temp2

                temp3 = dist_novo[n]
                dist_novo[n] = dist_novo[x]
                dist_novo[x] = temp3
    # Apresentação dos resultados da recomendação
    print('\n+++++     Recomendações     +++++\n')
    linha = ('='*30)
    for n in range(len(rest_b4)):
        print(f'Restaurante: {rest_novo[n]}\nNota: {ranking_novo[n]}\nDistância {dist_novo[n]}\n')
        print(linha)

def recomendar_b5 ():

    # Listas vazias que serão usadas na ordenação do ranking e exibição no output final
    rest_novo = []
    ranking_novo = []
    dist_novo = []

    # Comando para criação da nova lista que gera a saída de dados ordenadamente
    for n in rest_b5:
        rest_novo.append(n)

    for n in ranking_b5:
        ranking_novo.append(n)

    for n in dist_b5:
        dist_novo.append(n)

    # Algoritimo que valida ranking e distancia, em caso de empate nos rankings
    for n in range(len(rest_b5)):
        for x in range(n+1,len(rest_b5)):

            # Critério de desempate por distância entre restaurantes com o mesmo ranking
            if ranking_novo[n] == ranking_novo[x]:
                if dist_novo[n] > dist_novo[x]:

                    temp_1 = rest_novo[n]
                    rest_novo[n] = rest_novo[x]
                    rest_novo[x] = temp_1

                    temp_2 = ranking_novo[n]
                    ranking_novo[n] = ranking_novo[x]
                    ranking_novo[x] = temp_2

                    temp_3 = dist_novo[n]
                    dist_novo[n] = dist_novo[x]
                    dist_novo[x] = temp_3

            # Verificador do ranking do restaurante e ordenação da sequência de recomendações
            elif ranking_novo[n] < ranking_novo[x]:

                temp1 = rest_novo[n]
                rest_novo[n] = rest_novo[x]
                rest_novo[x] = temp1

                temp2 = ranking_novo[n]
                ranking_novo[n] = ranking_novo[x]
                ranking_novo[x] = temp2

                temp3 = dist_novo[n]
                dist_novo[n] = dist_novo[x]
                dist_novo[x] = temp3
    # Apresentação dos resultados da recomendação
    print('\n+++++     Recomendações     +++++\n')
    linha = ('='*30)
    for n in range(len(rest_b5)):
        print(f'Restaurante: {rest_novo[n]}\nNota: {ranking_novo[n]}\nDistância {dist_novo[n]}\n')
        print(linha)

def recomendar_b6 ():

    # Listas vazias que serão usadas na ordenação do ranking e exibição no output final
    rest_novo = []
    ranking_novo = []
    dist_novo = []

    # Comando para criação da nova lista que gera a saída de dados ordenadamente
    for n in rest_b6:
        rest_novo.append(n)

    for n in ranking_b6:
        ranking_novo.append(n)

    for n in dist_b6:
        dist_novo.append(n)

    # Algoritimo que valida ranking e distancia, em caso de empate nos rankings
    for n in range(len(rest_b6)):
        for x in range(n+1,len(rest_b6)):

            # Critério de desempate por distância entre restaurantes com o mesmo ranking
            if ranking_novo[n] == ranking_novo[x]:
                if dist_novo[n] > dist_novo[x]:

                    temp_1 = rest_novo[n]
                    rest_novo[n] = rest_novo[x]
                    rest_novo[x] = temp_1

                    temp_2 = ranking_novo[n]
                    ranking_novo[n] = ranking_novo[x]
                    ranking_novo[x] = temp_2

                    temp_3 = dist_novo[n]
                    dist_novo[n] = dist_novo[x]
                    dist_novo[x] = temp_3

            # Verificador do ranking do restaurante e ordenação da sequência de recomendações
            elif ranking_novo[n] < ranking_novo[x]:

                temp1 = rest_novo[n]
                rest_novo[n] = rest_novo[x]
                rest_novo[x] = temp1

                temp2 = ranking_novo[n]
                ranking_novo[n] = ranking_novo[x]
                ranking_novo[x] = temp2

                temp3 = dist_novo[n]
                dist_novo[n] = dist_novo[x]
                dist_novo[x] = temp3
    # Apresentação dos resultados da recomendação
    print('\n+++++     Recomendações     +++++\n')
    linha = ('='*30)
    for n in range(len(rest_b6)):
        print(f'Restaurante: {rest_novo[n]}\nNota: {ranking_novo[n]}\nDistância {dist_novo[n]}\n')
        print(linha)

def recomendar_b7 ():

    # Listas vazias que serão usadas na ordenação do ranking e exibição no output final
    rest_novo = []
    ranking_novo = []
    dist_novo = []

    # Comando para criação da nova lista que gera a saída de dados ordenadamente
    for n in rest_b7:
        rest_novo.append(n)

    for n in ranking_b7:
        ranking_novo.append(n)

    for n in dist_b7:
        dist_novo.append(n)

    # Algoritimo que valida ranking e distancia, em caso de empate nos rankings
    for n in range(len(rest_b7)):
        for x in range(n+1,len(rest_b7)):

            # Critério de desempate por distância entre restaurantes com o mesmo ranking
            if ranking_novo[n] == ranking_novo[x]:
                if dist_novo[n] > dist_novo[x]:

                    temp_1 = rest_novo[n]
                    rest_novo[n] = rest_novo[x]
                    rest_novo[x] = temp_1

                    temp_2 = ranking_novo[n]
                    ranking_novo[n] = ranking_novo[x]
                    ranking_novo[x] = temp_2

                    temp_3 = dist_novo[n]
                    dist_novo[n] = dist_novo[x]
                    dist_novo[x] = temp_3

            # Verificador do ranking do restaurante e ordenação da sequência de recomendações
            elif ranking_novo[n] < ranking_novo[x]:

                temp1 = rest_novo[n]
                rest_novo[n] = rest_novo[x]
                rest_novo[x] = temp1

                temp2 = ranking_novo[n]
                ranking_novo[n] = ranking_novo[x]
                ranking_novo[x] = temp2

                temp3 = dist_novo[n]
                dist_novo[n] = dist_novo[x]
                dist_novo[x] = temp3
    # Apresentação dos resultados da recomendação
    print('\n+++++     Recomendações     +++++\n')
    linha = ('='*30)
    for n in range(len(rest_b7)):
        print(f'Restaurante: {rest_novo[n]}\nNota: {ranking_novo[n]}\nDistância {dist_novo[n]}\n')
        print(linha)