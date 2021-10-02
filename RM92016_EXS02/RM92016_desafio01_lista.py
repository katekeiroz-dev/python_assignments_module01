
notaSalaImpar = []
notaSalaPar = []

soma = 0

opcao = -1
while opcao != 5:
    print('Digite: \n 1 - informar nota do aluno IMPARES \n 2 - informar nota do aluno PARES \n 3 - Exibir notas dos '
          'alunos '
          '\n 4 - Calcular média das sala '
          '\n 5 - '
          'Verificar qual sala tem maior média \n - 5 Sair do programa')
    opcao = int(input('Escolha sua opção: '))


if opcao == 1:
    print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES')

    for impar in range(1,50,2):
        notaSalaImpar.append(float(input(f'Digite a nota do aluno {impar}º:')))


elif opcao == 2:
    print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES')

    for par in range(2, 51, 2):
        notaSalaPar.append(float(input(f'Digite a nota do aluno {par}º:')))


elif opcao == 3:
    print(notaSalaImpar)
    print('--'*40)
    print(notaSalaPar)

elif opcao == 4:
    mediaImpar = sum(notaSalaImpar)/len(notaSalaImpar)
    mediaPar = sum(notaSalaPar)/len(notaSalaPar)
    print(f'A MÉDIA DA SALA IMPAR É :{mediaImpar:.1f}')
    print(f'A MÉDIA DA SALA PAR É :{mediaPar:.1f}')

