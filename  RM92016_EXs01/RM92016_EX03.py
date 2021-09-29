#Crie um algoritmo onde o usuário possa digitar o voto de cada um dos 5 membros da equipe e,
# ao final, exiba qual foi o console escolhido e com quantos votos.
#As opções são: PLAYSTATION, XBOX e NINTENDO.


console1 = int(input('Qual console recebeu mais votos: 1-PLAYSTATION ____\n (chute um númeroo de 0 - 5)  '))
console2 = int(input('Qual console recebeu mais votos: 1-XBOX ____\n (chute um númeroo de 0 - 5)  '))
console3 = int(input('Qual console recebeu mais votos: 1-NINTENDO ____\n (chute um númeroo de 0 - 5)  '))

console = console2

if console2 ==4:
    print(f"Parabéns, você acertou! \n O console mais votado com {console} votos foi XBOX")
else:
    print(f"Você não acertou nenhuma das quantidades de voto !\n"
          f" O console mais votado com {console} votos foi XBOX")

