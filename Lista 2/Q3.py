X = int(input())
P = 0
num = 1

while num > 0:
    num = int(input())
    soma = 0
    
    if num > 0:
        for i in range(1, num+1):
            soma += i
        
        else:
            P += soma

else:
    if P < X:
        print("Ainda nos falta um pouco...")
    
    elif P == X:
        print("Pode beijar a noiva, afinal, vocês conseguiram!")
    
    elif P > X:
        R = P - X
        if R < 20 * X:
            print("Parece que os pombinhos passaram um pouco do local...")
            
        elif R >= 20 * X and R <= 100 * X:
            print("Acho que nos perdemos um pouco no caminho, onde estamos?")
        
        elif R > 100 * X:
            print("Hum... acho que o casal deve rever seus votos de matrimônio...")