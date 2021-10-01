#1 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por
# essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você
# criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos
# que tem número ímpar na chamada (1, 3, 5, ..., 47, 49) e depois as notas dos 25 alunos que tem número par
# (2, 4, 6,..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final,
# qual delas teve a maior nota.
#Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas
# deve ser exibida uma mensagem no seguinte padrão:
#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.



soma = 0
print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES')
for impar in range(1,26,2):
    alunosImpar = float(input(f'Digite nota do aluno {impar}º:'))
    soma = soma + 1
    mediaImpar = soma + alunosImpar / 13

print(f'A MEDIA DA SALA IMPAR É :{mediaImpar:.1f}')

print('_'*40)
print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES')

for impar in range(2,25,2):
    alunosPar = float(input(f'Digite nota do aluno {impar}º:'))
    soma = soma + 1
    mediaPar = soma + alunosPar / 12

print(f'A MEDIA DA SALA PAR É :{mediaPar:.1f}')

if mediaImpar > mediaPar:
    print('A sala com maior media eh IMPAR')
else:
    print('A sala com maior media eh PAR')