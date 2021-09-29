pacote = float(input('Qual o valor da passagem?'))
assento = int(input(' Escolha a categoria do seu assento :\n 1- Econômica / 2- Executiva / 3- Primeira Classe\n '
                    '(digite o número que corresponde a categoria , ex 1 , 2 ou 3)'))
viajantes = int(input('Número de pessoas que irão viajar?'))

if assento == 0:
    print('Por favor informe a categoria do assento correta !')
elif assento == 1 and viajantes == 2:
    desconto = 3
    total = pacote - 1.5
    mediaPassageiro = total / viajantes
    print(f" Valor da passagem: {float(pacote):.2f}R$\n Valor do desconto: {int(desconto)}% \n VALOR FINAL : "
          f"{float(total):.2f} R$ \n Total media por passageiro : {float(mediaPassageiro):.2f} " + "R$")
elif assento == 1 and viajantes == 3:
    desconto = 4
    total = pacote - 2
    mediaPassageiro = total / viajantes
    print(f" Valor da passagem: {float(pacote):.2f}R$\n Valor do desconto: {int(desconto)}% \n VALOR FINAL : "
          f"{float(total):.2f} R$ \n Total media por passageiro : {float(mediaPassageiro):.2f} " + "R$")
# executiva
elif (assento == 1 and viajantes >= 4) or (assento == 2 and viajantes ==2):
    desconto = 5
    total = pacote - 2.5
    mediaPassageiro = total / viajantes
    print(f" Valor da passagem: {float(pacote):.2f}R$\n Valor do desconto: {int(desconto)}% \n VALOR FINAL : "
          f"{float(total):.2f} R$ \n Total media por passageiro : {float(mediaPassageiro):.2f} " + "R$")
elif assento == 2 and viajantes == 3:
    desconto = 7
    total = pacote - 3.5
    mediaPassageiro = total / viajantes
    print(f" Valor da passagem: {float(pacote):.2f}R$\n Valor do desconto: {int(desconto)}% \n VALOR FINAL : "
          f"{float(total):.2f} R$ \n Total media por passageiro : {float(mediaPassageiro):.2f} " + "R$")
elif assento == 2 and viajantes >= 4:
    desconto = 8
    total = pacote - 4
    mediaPassageiro = total / viajantes
    print(f" Valor da passagem: {float(pacote):.2f}R$\n Valor do desconto: {int(desconto)}% \n VALOR FINAL : "
          f"{float(total):.2f} R$ \n Total media por passageiro : {float(mediaPassageiro):.2f} " + "R$")

#Primeira classe
elif assento == 3 and viajantes == 2:
    desconto = 10
    total = pacote - 50
    mediaPassageiro = total / viajantes
    print(f" Valor da passagem: {float(pacote):.2f}R$\n Valor do desconto: {int(desconto)}% \n VALOR FINAL : "
          f"{float(total):.2f} R$ \n Total media por passageiro : {float(mediaPassageiro):.2f} " + "R$")
elif assento == 3 and viajantes == 3:
    desconto = 15
    total = pacote - 75
    mediaPassageiro = total / viajantes
    print(f" Valor da passagem: {float(pacote):.2f}R$\n Valor do desconto: {int(desconto)}% \n VALOR FINAL : "
          f"{float(total):.2f} R$ \n Total media por passageiro : {float(mediaPassageiro):.2f} " + "R$")
elif assento == 3 and viajantes >= 4:
    desconto = 20
    total = pacote - 100
    mediaPassageiro = total / viajantes
    print(f" Valor da passagem: {float(pacote):.2f}R$\n Valor do desconto: {int(desconto)}% \n VALOR FINAL : "
          f"{float(total):.2f} R$ \n Total media por passageiro : {float(mediaPassageiro):.2f} " + "R$")
else:
    print('Informaçōes incorretas ! Por favor tente novamente.')