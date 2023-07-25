# 1 = armadilha na esquerda
# 2 = armadilha na direita
ponte = {}
# {numero do jogador: [nome, apelido, status, posicao atual]}
jogadores = {}
flag = True
contador = 1
casas = int(input())

if casas >= 2 and casas <= 10:
    for i in range(casas):
        casa = int(input())
        ponte.update({i+1: casa})
    
    for i in range(3):
        nome = input()
        apelido = input()
        jogadores.update({i+1: [nome, apelido, "vivo", 0]})

    while flag:
        if contador == 4:
            contador = 1

        if jogadores.get(contador)[2] == "vivo":
            escolha = int(input())
            atual = jogadores.get(contador)[3] + 1

            if ponte.get(atual) == escolha: # erro
                jogadores.update({contador: [jogadores.get(contador)[0], jogadores.get(contador)[1], "morto", jogadores.get(contador)[3]+1]})
                
                if jogadores.get(1)[2] == "morto" and jogadores.get(2)[2] == "morto" and jogadores.get(3)[2] == "morto":
                    print("Todos os jogadores morreram!")
                    flag = False
                else:
                    print(f"{jogadores.get(contador)[0]} caiu de uma altura de 30 metros e morreu! :O")

            else:
                jogadores.update({contador: [jogadores.get(contador)[0], jogadores.get(contador)[1], jogadores.get(contador)[2], jogadores.get(contador)[3]+1]})

                if jogadores.get(contador)[3] == casas:
                    print(f"{jogadores.get(contador)[0]}, mais conhecido como {jogadores.get(contador)[1]}, ganhou o jogo! Parabéns!")
                    flag = False
                else:
                    print(f"{jogadores.get(contador)[0]} pulou uma casa!")
        contador+=1

else:
    print("Faixa não permitida")