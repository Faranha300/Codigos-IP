N = input()
X = int(input())
qtdV = 0

while X > 0:
    nome, palavra = input().split("-")
    qtd = 0
    
    for i in palavra:
        if N == i:
            qtd += 1
    
    else:
        if qtd > qtdV:
            qtdV = qtd
            nomeV = nome
            palavraV = palavra
    
    X -= 1
    
else:
    if nomeV == "Prior":
        print(f"Joga y joga! Mago Prior e o novo lider com a palavra {palavraV} com {qtdV} aparicoes da letra {N}.")
        
    else:
        print(f"Vish! O Mago Prior pode ir pro paredao, ja que quem ganhou foi {nomeV}, com a palavra {palavraV} e {qtdV} aparicoes da letra {N}.")