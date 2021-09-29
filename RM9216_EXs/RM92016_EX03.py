#3 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a
# realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que
# cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira)
# obtiveram, verifique e exiba qual dia foi o escolhido.

valor = print(input('Fizemos uma votação para escolher qual o melhor dia da semana para a realização das '
                    'lives.\n Quantos votos você acha que cada dia da semana obteve? \n'
                    '(Aperte ENTER para continuar)'))


seg = int(input('Quantos votos para : SEGUNDA- FEIRA'))
votos1 = 30
ter = int(input('Quantos votos para : TERÇA- FEIRA'))
votos2 = 48
qua = int(input('Quantos votos para : QUARTA- FEIRA'))
votos3 = 20
qui = int(input('Quantos votos para : QUINTA- FEIRA'))
votos4 = 60
sex = int(input('E por fim, quantos votos para : SEXTA- FEIRA'))
votos5 = 8


if qui ==60:
    print(f"Parabéns, você acertou! \n O dia mais votado com {votos4} votos foi QUINTA-FEIRA")
else:
    print(f"Você não acertou nenhuma das quantidades de voto !\n"
          f" O dia mais votado com {votos4} votos foi QUINTA-FEIRA")

