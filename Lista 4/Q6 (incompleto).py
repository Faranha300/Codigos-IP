def inserirMatriz(X, Y, matriz, representacao):
    matriz[X].insert(Y+1, representacao)
    matriz[X].remove("-")

def jogadorMovimentoHorizontal(jogadorX, jogadorY, objetivo, matriz):
    if jogadorY > objetivo:
        matriz[jogadorX].remove("V")
        jogadorY -= 1
        matriz[jogadorX].insert(jogadorY, "V")
        
    else:
        matriz[jogadorX].remove("V")
        jogadorY += 1
        matriz[jogadorX].insert(jogadorY, "V")

    if matriz[jogadorX][jogadorY + 1] == "G":
        matriz[jogadorX].remove("G")
        return jogadorY, "gasolina"
        
    elif matriz[jogadorX][jogadorY + 1] == "C":
        matriz[jogadorX].remove("C")
        return jogadorY, "carro"
        
    else:
        return jogadorY, ""

def jogadorMovimentoVertical(jogadorX, jogadorY, objetivo, matriz):# Depois de pegar a gasolina fica parado 1 turno
    if jogadorX > objetivo:
        matriz[jogadorX].remove("V")
        matriz[jogadorX].append("-")
        jogadorX -=1
        matriz[jogadorX].insert(jogadorY, "V")
    
    else:
        matriz[jogadorX].remove("V")
        matriz[jogadorX].append("-")
        jogadorX += 1
        matriz[jogadorX].insert(jogadorY, "V")
    
    if matriz[jogadorX][jogadorY + 1] == "G":
        matriz[jogadorX].remove("G")
        return jogadorX, "gasolina"
        
    elif matriz[jogadorX][jogadorY + 1] == "C":
        matriz[jogadorX].remove("C")
        return jogadorX, "carro"
        
    else:
        matriz[jogadorX].remove("-")
        return jogadorX, ""

def jasonMovimentoHorizontal(jasonX, jasonY, objetivo, matriz):
    if jasonY > objetivo:
        matriz[jasonX].remove("J")
        jasonY -= 1
        matriz[jasonX].insert(jasonY, "J")

    else:
        matriz[jasonX].remove("J")
        jasonY += 1
        matriz[jasonX].insert(jasonY, "J")

    return jasonY

def jasonMovimentoVertical(jasonX, jasonY, objetivo, matriz):
    pass

def distancia(jogadorX, jogadorY, jasonX, jasonY):
    result = int(((jogadorX - jasonX)**2 + (jogadorY - jasonY)**2)**0.5)
    return result

matriz = [["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"]]
jogadorX = int(input())
jogadorY = int(input())
jasonX = int(input())
jasonY = int(input())
gasolinaX = int(input())
gasolinaY = int(input())
carroX = int(input())
carroY = int(input())
pegou = False
parado = False
flag = True

inserirMatriz(jogadorX, jogadorY, matriz, "V")
inserirMatriz(jasonX, jasonY, matriz, "J")
inserirMatriz(gasolinaX, gasolinaY, matriz, "G")
inserirMatriz(carroX, carroY, matriz, "C")

while flag:
    if jasonY == jogadorY:
        jasonX = jasonMovimentoVertical(jasonX, jasonY, jogadorX, matriz)
    else:
        jasonY = jasonMovimentoHorizontal(jasonX, jasonY, jogadorY, matriz)

    if pegou:
        if not parado:
            if jogadorY == carroY:
                jogadorX, acontecimento = jogadorMovimentoVertical(jogadorX, jogadorY, carroX, matriz)
            else:
                jogadorY, acontecimento = jogadorMovimentoHorizontal(jogadorX, jogadorY, carroY, matriz)
    else:
        if jogadorY == gasolinaY:
            jogadorX, acontecimento = jogadorMovimentoVertical(jogadorX, jogadorY, gasolinaX, matriz)
        else:
            jogadorY, acontecimento = jogadorMovimentoHorizontal(jogadorX, jogadorY, gasolinaY, matriz)

    # Outputs
    for i in matriz:
        x = " ".join(i)
        print(x)

    if acontecimento == "":
        print("Nao peguei nenhum objeto nessa rodada :(")
    elif acontecimento == "gasolina":
        print("Deu bom! Peguei a Gasolina nessa rodada.")
    elif acontecimento == "carro":
        print("Consegui chegar no carro, agora e so ligar e fugir daqui!")
        flag = False

    if jasonX == jogadorX and jasonY == jogadorY:
        print("Oh nao, o Jason me pegou, F total!")
        flag = False

    else:
        distanciaJJ = distancia(jogadorX, jogadorY, jasonX, jasonY)
        if distanciaJJ <= 3:
            print("E melhor correr, o Jason vai me pegar!\n")
        elif distanciaJJ <= 4:
            print("Consigo ver o Jason daqui, preciso apressar o passo!\n")
        else:
            print("Ufa, o Jason ainda esta longe, mas nao posso diminuir o ritmo.\n")
            
    if acontecimento == "gasolina":
        pegou = True
        parado = True
        
    parado = False