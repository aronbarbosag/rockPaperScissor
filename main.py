import random
from artes import logo
from artes import opcoes

print(logo)
playing = True

while playing:
    personChoose = int(
        input("Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura: "))
    machineChoose = random.randint(0, 2)
    print("Você escolheu: ")
    print(opcoes[personChoose])
    print("A maquina escolheu:")
    print(opcoes[machineChoose])

    #logica do jogo
    if personChoose == machineChoose:
        print("Empate!!")

    #jogador ganha quando
    #pedra(0) ganha de tesoura(2)
    #tesoura(2) ganha de papel(1)
    #papel(1) ganha de pedra(0)
    if personChoose != machineChoose:
        if personChoose == 0 and machineChoose == 2 or personChoose > machineChoose:
            print("Você ganhou!!")

        else:
            print("Você perdeu!!")

    playing = bool(
        int(input(
            "Deseja jogar novamente? Digite 1 para sim ou 0 para nao: ")))

print("Fim do Jogo! Obrigado por jogar!!")
