# Função para fazer o calculo de fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))
        
# Função pra calcular a barra de vida do jogador
def calcularBarraVida(vida, barra, vidaBase):
    vidaBarra = vida / 10

    if vidaBarra == vidaBase * 10:
        vidaBarra = int(vidaBarra)
        
    elif vidaBarra <= 0:
        vidaBarra = int(vidaBarra)
        
    elif vidaBarra - int(vidaBarra) == 0:
        vidaBarra = int(vidaBarra)

    else:
        vidaBarra += 1
        vidaBarra = int(vidaBarra)

    for i in range(vidaBarra): # Tem que sempre ter 10 caracteres
        barra.append("*")

    tracos = (vidaBase * 10) - len(barra)

    if tracos >= 1:
        for i in range(tracos):
            barra.append("-")
    
    return barra
# Função da luta
def luta(nome1, ataque1, defesa1, ataqueEspecial1, vida1, nome2, ataque2, defesa2, ataqueEspecial2, vida2, vidaBase, round):
    barra1 = []
    barra2 = []
    result = 0
    
    if round >= 5: # A partir do round 5 o atacante pode atacar com o especial
        if round % 2 == 1: # jogador 1 ataca
            result = fibonacci(round - 1)
                
            if result % 2 == 0: # se fibonacci for par ataca com o especial
                dano = ataqueEspecial1
                vida2 -= dano
            else:
                dano = ataque1 - defesa2
                vida2 -= dano

        elif round % 2 == 0: # jogador 2 ataca
            result = fibonacci(round - 1)
                
            if result % 2 == 0:
                dano = ataqueEspecial2
                vida1 -= dano
            else:
                dano = ataque2 - defesa1
                vida1 -= dano
                
    else:
        if round % 2 == 1:
            dano = ataque1 - defesa2
            vida2 -= dano

        elif round % 2 == 0:
            dano = ataque2 - defesa1
            vida1 -= dano

    barra1 = calcularBarraVida(vida1, barra1, vidaBase)
    barra2 = calcularBarraVida(vida2, barra2, vidaBase)

    # OUTPUT
    print(f"\nROUND {round}:")
    print(f"VIDA {nome1}:")
    print(" ".join(barra1))
    print(f"VIDA {nome2}:")
    print(" ".join(barra2))
    # OUTPUT

    if vida1 <= 0:
        return nome2
    elif vida2 <= 0:
        return nome1
    else:
        return luta(nome1, ataque1, defesa1, ataqueEspecial1, vida1, nome2, ataque2, defesa2, ataqueEspecial2, vida2, vidaBase, round + 1)

# INPUT
nome1 = input()
ataque1 = int(input())
defesa1 = int(input())
ataqueEspecial1 = int(input())
nome2 = input()
ataque2 = int(input())
defesa2 = int(input())
ataqueEspecial2 = int(input())
vidaBase = int(input())
# INPUT
vida1 = vidaBase * 100
vida2 = vidaBase * 100
round = 1

ganhador = luta(nome1, ataque1, defesa1, ataqueEspecial1, vida1, nome2, ataque2, defesa2, ataqueEspecial2, vida2, vidaBase, round)

print(f"O vencedor da luta foi {ganhador}") # OUTPUT