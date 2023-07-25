BethR = int(input())
AdvR = int(input())
resultadoP = str(input())

E = 1 / (1 + 10 ** ((AdvR - BethR)/400))

if resultadoP == "vitoria":
    BethR = BethR + 40 * (1 - E)
    print(f"O novo rating da Beth Harmon é {int(BethR)}")
    
elif resultadoP == "empate":
    BethR = BethR + 40 * (0.5 - E)
    print(f"O novo rating da Beth Harmon é {int(BethR)}")
    
elif resultadoP == "derrota":
    BethR = BethR + 40 * (0 - E)
    print(f"O novo rating da Beth Harmon é {int(BethR)}")
    
else:
    print("Resultado da partida invalido")