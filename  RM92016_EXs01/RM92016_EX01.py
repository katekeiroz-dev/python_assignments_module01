#verificar se os batimentos cardíacos por minuto se encontram na faixa adequada.
# Para isso, você deve solicitar que o usuário informe o seu número de BATIMENTOS POR MINUTO (BPM)
# e a IDADE. A partir disso o script deva verificar e exibir uma mensagem informando se os batimentos
# do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada):



bpm = int(input('Por favor, informe o seu BPM (batimentos por minutos):'))
idade = int(input('Informe agora, sua IDADE :'))


#crianca
if idade == 2 and (bpm ==120 and bpm <= 140):
    print('Seu BPM encontram-se DENTRO da faixa adequada.')
elif idade == 2 and bpm > 140:
    print('Seu BPM encontram-se ACIMA da faixa adequada.')
elif idade ==2 and bpm < 120:
    print('Seu BPM encontram-se ABAIXO da faixa adequada.')

#adulto,idoso
elif (idade >= 8 and idade <= 65 and bpm >= 70 and bpm <= 100) or (idade > 65 and bpm >= 50 and bpm <= 60):
    print('Seu BPM encontram-se DENTRO da faixa adequada.')

elif (idade >= 8 and idade <= 65 and bpm > 100) or (idade > 65 and bpm > 60):
    print('Seu BPM encontram-se ACIMA da faixa adequada.')

elif (idade >= 8 and idade <= 65 and bpm < 70) or (idade > 65 and bpm < 50):
    print('Seu BPM encontram-se ABAIXO da faixa adequada.')