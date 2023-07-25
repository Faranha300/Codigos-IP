# Inicio Input
nome_1 = str(input())
vida_1 = int(input())
ataque_1 = int(input())
defesa_1 = int(input())

nome_2 = str(input())
vida_2 = int(input())
ataque_2 = int(input())
defesa_2 = int(input())

# Fim Input

print("Round 1")  # Round 1

golpe = str(input())
defesa = str(input())

if golpe == "jab":
    if defesa == "bloqueio":
        dano = (ataque_1 - (ataque_1 * (defesa_2/100)))
        vida_2 = vida_2 - dano

    elif defesa == "esquiva":
        ataque_2 = ataque_2 + (ataque_2 * 0.10)

    elif defesa == "X":
        vida_2 = vida_2 - ataque_1

elif golpe == "direto":
    if defesa == "bloqueio":
        dano = (ataque_1 * 1.3 - (ataque_1 * defesa_2/100))
        vida_2 = vida_2 - dano

    elif defesa == "esquiva":
        ataque_2 = ataque_2 + (ataque_2 * 0.20)

    elif defesa == "X":
        vida_2 = vida_2 - ataque_1 * 1.4

# Verificando se alguém ganhou no Round 1

if vida_2 <= 0:
    print(
        f"NOSSO CAMPEAO E {nome_1.upper()} COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND")

else:
    print("Round 2")  # Round 2

    golpe = str(input())
    defesa = str(input())

    if golpe == "jab":
        if defesa == "bloqueio":
            dano = (ataque_2 - (ataque_2 * (defesa_1/100)))
            vida_1 = vida_1 - dano

        elif defesa == "esquiva":
            ataque_1 = ataque_1 + (ataque_1 * 0.10)

        elif defesa == "X":
            vida_1 = vida_1 - ataque_2

    elif golpe == "direto":
        if defesa == "bloqueio":
            dano = (ataque_2 * 1.3 - (ataque_2 * defesa_1/100))
            vida_1 = vida_1 - dano

        elif defesa == "esquiva":
            ataque_1 = ataque_1 + (ataque_1 * 0.20)

        elif defesa == "X":
            vida_1 = vida_1 - ataque_2 * 1.4

    # Verificando se alguém ganhou no Round 2

    if vida_1 <= 0:
        print(f"NOSSO CAMPEAO E {nome_2.upper()}")

    else:
        print("Round 3")  # Round 3
        print(f"{nome_1.upper()} SO TEM MAIS UM ROUND PARA DERRUBAR SEU ADVERSARIO")

        golpe = str(input())
        defesa = str(input())

        if golpe == "jab":
            if defesa == "bloqueio":
                dano = (ataque_1 - (ataque_1 * (defesa_2/100)))
                vida_2 = vida_2 - dano

            elif defesa == "esquiva":
                ataque_2 = ataque_2 + (ataque_2 * 0.10)

            elif defesa == "X":
                vida_2 = vida_2 - ataque_1

        elif golpe == "direto":
            if defesa == "bloqueio":
                dano = (ataque_1 * 1.3 - (ataque_1 * defesa_2/100))
                vida_2 = vida_2 - dano

            elif defesa == "esquiva":
                ataque_2 = ataque_2 + (ataque_2 * 0.20)

            elif defesa == "X":
                vida_2 = vida_2 - ataque_1 * 1.4
                
        if vida_2 <= 0:
            print(f"NOSSO CAMPEAO E {nome_1.upper()}")
            
        else:
            print(f"NOSSO CAMPEAO E {nome_2.upper()}")