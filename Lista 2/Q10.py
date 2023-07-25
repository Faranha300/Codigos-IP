lucasV = 100
severinoV = 100
N = 1
T = 0
efeito1 = 0
efeito2 = 0

while N <= 12 and lucasV >= 0 and severinoV >= 0:
    acao1 = str(input())
    acao2 = str(input())
    
    if N == 4:
        T = lucasV
        lucasV = severinoV
        severinoV = T
        
    elif N == 7:
        efeito1 = efeito1 + ((1/2) * efeito1) + ((1/4) * efeito1)
        efeito2 = efeito2 + ((1/2) * efeito2) + ((1/4) * efeito2)
        lucasV -= efeito1
        severinoV -= efeito2
    
    elif N == 10:
        if lucasV > severinoV:
            severinoV = lucasV
        else:
            lucasV = severinoV
    
    else:
        if acao1 == "Golpe Rapido":
            if acao2 == "Golpe Rapido":
                lucasV -= 12
                severinoV -= 12
                if N == 6:
                    efeito1 = 12
                    efeito2 = 12
            elif acao2 == "Bloqueio":
                severinoV -= 6
                if N == 6:
                    efeito2 = 6
            elif acao2 == "Esquivar":
                severinoV -= 12
                if N == 6:
                    efeito2 = 12
            elif acao2 == "Golpe Forte":
                lucasV -= 25
                severinoV -= 12
                if N == 6:
                    efeito1 = 25
                    efeito2 = 12
    
        elif acao1 == "Golpe Forte":
            if acao2 == "Golpe Rapido":
                lucasV -= 12
                severinoV -= 25
                if N == 6:
                    efeito1 = 12
                    efeito2 = 25
            elif acao2 == "Bloqueio":
                severinoV -= 20
                if N == 6:
                    efeito2 = 20
            elif acao2 == "Esquivar":
                lucasV -= 20
                if N == 6:
                    efeito1 = 20
                
        elif acao1 == "Bloqueio":
            if acao2 == "Golpe Rapido":
                lucasV -= 6
                if N == 6:
                    efeito1 = 6
            elif acao2 == "Golpe Forte":
                lucasV -= 20
                if N == 6:
                    efeito1 = 20
            
        elif acao1 == "Esquiva":
            if acao2 == "Golpe Rapido":
                lucasV -= 12
                if N == 6:
                    efeito1 = 12
            elif acao2 == "Golpe Forte":
                severinoV -= 20
                if N == 6:
                    efeito2 = 20
    
    N += 1
    
else:
    if lucasV <= 0 and severinoV > 0:
        print("Foi uma prova dificil, mas Severino mostra como se faz e vence o BBCIn do 2021.2!!")
    elif severinoV <= 0 and lucasV > 0:
        print("Foi uma prova dificil, mas Lucas mostra como se faz e vence o BBCIn do 2021.2!!")
    elif (lucasV == severinoV) or (lucasV < severinoV and severinoV <= 0) or (severinoV < lucasV and lucasV <= 0):
        print("Pela primeira vez na historia, ha um empate e ambos irao levar para casa o grande premio do BBCIn do 2021.2!!")
    elif N >= 12:
        if lucasV > severinoV:
            print("Foi uma prova dificil, mas Lucas mostra como se faz e vence o BBCIn do 2021.2!!")
        else:
            print("Foi uma prova dificil, mas Severino mostra como se faz e vence o BBCIn do 2021.2!!")