min = int(input('Digite os minutos (entre 0 e 59) '))
fato = 1
while min >= 1:
    fato = fato * min
    min = min - 1

print(f'LIBERDADE{fato}')