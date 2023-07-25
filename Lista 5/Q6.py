# Sul > Leste > Norte > Oeste
# Função que faz o Link andar
def sul(labirinto, X, Y):
    Y += 1
    labirinto[Y][X] = "L"
            
    for i in labirinto:
        print("".join(i))
    print("Caminharei pelo Sul e certamente irei encontrar-te, Zelda\n")
    return labirinto, X, Y

def leste(labirinto, X, Y):
    X += 1
    labirinto[Y][X] = "L"
    
    for i in labirinto:
        print("".join(i))
    print("Caminharei pelo Leste e certamente irei encontrar-te, Zelda\n")
    return labirinto, X, Y

def norte(labirinto, X, Y):
    Y -= 1
    labirinto[Y][X] = "L"
    
    for i in labirinto:
        print("".join(i))
    print("Caminharei pelo Norte e certamente irei encontrar-te, Zelda\n")
    return labirinto, X, Y

def oeste(labirinto, X, Y):
    X -= 1
    labirinto[Y][X] = "L"

    for i in labirinto:
        print("".join(i))
    print("Caminharei pelo Oeste e certamente irei encontrar-te, Zelda\n")
    return labirinto, X, Y

def andar(labirinto, X, Y, ZeldaX, ZeldaY, tam):
    if X == ZeldaX and Y == ZeldaY:
        return True

    if X < tam and Y < tam and X != 0 and Y != 0:
        if labirinto[Y+1][X] == "." or labirinto[Y+1][X] == "Z":
            labirinto, X, Y = sul(labirinto, X, Y)
            return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)

        elif labirinto[Y][X+1] == "." or labirinto[Y][X+1] == "Z":
            labirinto, X, Y = leste(labirinto, X, Y)
            return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)

        elif labirinto[Y-1][X] == "." or labirinto[Y-1][X] == "Z":
            labirinto, X, Y = norte(labirinto, X, Y)
            return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)

        elif labirinto[Y][X-1] == "." or labirinto[Y][X-1] == "Z":
            labirinto, X, Y = oeste(labirinto, X, Y)
            return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)

        else:
            return False
    
    else:
        if Y == tam:
            if (labirinto[Y][X+1] == "#" or labirinto[Y][X+1] == "L") and (labirinto[Y-1][X] == "#" or labirinto[Y-1][X] == "L") and (labirinto[Y][X-1] == "#" or labirinto[Y][X-1] == "L"):
                return False
            else:
                if labirinto[Y][X+1] == "." or labirinto[Y][X+1] == "Z":
                    labirinto, X, Y = leste(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                elif labirinto[Y-1][X] == "." or labirinto[Y-1][X] == "Z":
                    labirinto, X, Y = norte(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                elif labirinto[Y][X-1] == "." or labirinto[Y][X-1] == "Z":
                    labirinto, X, Y = oeste(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                else:
                    return False

        elif X == tam:
            if (labirinto[Y+1][X] == "#" or labirinto[Y+1][X] == "L") and (labirinto[Y-1][X] == "#" or labirinto[Y-1][X] == "L") and (labirinto[Y][X-1] == "#" or labirinto[Y][X-1] == "L"):
                return False
            else:
                if labirinto[Y+1][X] == "." or labirinto[Y+1][X] == "Z":
                    labirinto, X, Y = sul(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                elif labirinto[Y-1][X] == "." or labirinto[Y-1][X] == "Z":
                    labirinto, X, Y = norte(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                elif labirinto[Y][X-1] == "." or labirinto[Y][X-1] == "Z":
                    labirinto, X, Y = oeste(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                else:
                    return False

        elif X == 0:
            if (labirinto[Y+1][X] == "#" or labirinto[Y+1][X] == "L") and (labirinto[Y][X+1] == "#" or labirinto[Y][X+1] == "L") and (labirinto[Y-1][X] == "#" or labirinto[Y-1][X] == "L"):
                return False
            else:
                if labirinto[Y+1][X] == "." or labirinto[Y+1][X] == "Z":
                    labirinto, X, Y = sul(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                elif labirinto[Y][X+1] == "." or labirinto[Y][X+1] == "Z":
                    labirinto, X, Y = leste(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                elif labirinto[Y-1][X] == "." or labirinto[Y-1][X] == "Z":
                    labirinto, X, Y = norte(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                else:
                    return False

        elif Y == 0:
            if (labirinto[Y+1][X] == "#" or labirinto[Y+1][X] == "L") and (labirinto[Y][X+1] == "#" or labirinto[Y][X+1] == "L") and (labirinto[Y][X-1] == "#" or labirinto[Y][X-1] == "L"):
                return False
            else:
                if labirinto[Y+1][X] == "." or labirinto[Y+1][X] == "Z":
                    labirinto, X, Y = sul(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                elif labirinto[Y][X+1] == "." or labirinto[Y][X+1] == "Z":
                    labirinto, X, Y = leste(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                elif labirinto[Y][X-1] == "." or labirinto[Y][X-1] == "Z":
                    labirinto, X, Y = oeste(labirinto, X, Y)
                    return andar(labirinto, X, Y, ZeldaX, ZeldaY, tam)
                
                else:
                    return False

N = int(input())
Coord1 = int(input())
Coord2 = int(input())
labirinto = []

for i in range(N):
    forcount = 0
    linha = input()
    forlinha = []
    for j in linha:
        if j == "Z":
            ZeldaX = forcount
            ZeldaY = i
        forlinha.append(j)
        forcount += 1
    labirinto.append(forlinha)


if andar(labirinto, Coord2, Coord1, ZeldaX, ZeldaY, N-1):
    for i in labirinto:
        print("".join(i))
    print("Vamos embora daqui Princesa!!!")

else:
    print("HAHAHAHA você nunca irá resgatá-la, Link!!!")