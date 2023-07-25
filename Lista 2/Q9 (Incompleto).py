palavra = "PROVA-DO-ANJO-BBB"
palavraS = ""
vidas = 3
letras_digitadas = ""
letras_corretas = "PROVADNJB"
letras_acertadas = ""

while vidas > 0:
    letra = input().upper()
    N = 0
    V = 0
    
    for l in letras_digitadas:
        if l == letra:
            print(f"Voce ja digitou a letra {letra}")
        
    else:
        letras_digitadas += letra
        
        for x in letras_corretas:
            if x == letra:
                print("Parabens, voce conseguiu mais uma letra!")
                letras_acertadas += letra
                     
    palavraS = ""
    for l in letras_acertadas:
        for n in palavra:
            if l == n:
                palavraS += l
            
            else:
                palavraS += "-"
                
    for x in letras_corretas: # Uma letra errada q já foi digitada tá entrando aq
        if x != letra:
            N += 1
    
    else:
        if N == 9:
            vidas -= 1
            print(f"Que pena, voce tem mais {vidas} chances!")
    
    for x in letras_corretas: # Verificação se acertou todas as letras
        for l in letras_acertadas:
            if x == l:
                V += 1
    else:
        if V == 9:
            vidas = -1
    
    if palavraS == "":
        print("-----------------")
    else:
        print(palavraS)
                
else: 
    if vidas == 0: # Quando perder todas as vidas
        print("Fim de jogo, sem almoco do anjo pra voce!")
    
    elif vidas == -1:
        print("Boa, voce e o novo Anjo da semana!")