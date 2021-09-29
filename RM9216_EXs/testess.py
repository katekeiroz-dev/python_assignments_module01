
# desafio curso em video, algoritimos , somar juros de 20% em cima de um valor
# e dividir pelo numero de parcelas:)


emp = int(input('valor do emprestimo? '))
juros = (20 / 100.) * emp
total = juros + emp

parcelas = int(input('numero de parcelas:'))
valortotal = total / parcelas


print(int(valortotal))
