#Sua tarefa é criar um algoritmo que receba o tipo de assinatura
# do cliente, o faturamento anual dele e que calcule e exiba qual
# o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo
# mostra a porcentagem de acordo com cada nível de assinatura:

plano = int(input('Ola , escolha seu plano de assinatura: \n 1- Basic / 2- Silver / 3- Gold / 4- Platinum '))
faturamentoAnual = float(input('Informe agora o valor do seu faturamento anual: '))

if plano ==0:
    print('A opção escolhida está inválida,por favor escolha escolha outra opção')
elif plano==1:
    bonus = faturamentoAnual * 0.30
    print(f"O valor do bônus é de {float(bonus)}" + ' R$')
elif plano==2:
    bonus = faturamentoAnual * 0.20
    print(f"O valor do bônus é de {float(bonus)}" + ' R$')
elif plano==3:
    bonus = faturamentoAnual * 0.10
    print(f"O valor do bônus é de {float(bonus)}" + ' R$')
elif plano==4:
    bonus = faturamentoAnual * 0.05
    print(f"O valor do bônus é de {float(bonus)}" + ' R$')
