def roubo(descricao, arma, municao):
    if descricao == "arma":
        arma = "nada"
        return arma
    
    elif descricao == "municao":
        if arma == "Revolver":
            municao -= 6
            
        elif arma == "Bastard":
            municao -= 30
            
        elif arma == "Duplet":
            municao -= 2
        
        elif arma == "VSV":
            municao -= 21
        
        elif arma == "Kalash":
            municao -= 30
        
        return municao

def combate(nomeMonstro, qtd, arma, municao, vidaJogador, armas, monstros):
    if arma == "nada":
        return vida, municao, False, "sem arma"
    
    elif municao == 0:
        return vida, municao, False, "sem municao"
    
    else:
        for i in armas:
            if i == arma:
                ataqueJogador = armas[i][1]
                municaoPerdida = armas[i][2]
    
        for i in monstros:
            if i == nomeMonstro:
                ataqueMonstros = monstros[i][1] * qtd
                vidaMonstros = monstros[i][2] * qtd
    
        while vidaJogador > 0 or vidaMonstros > 0 or municao > 0:
            vidaMonstros -= ataqueJogador
            municao -= municaoPerdida
        
            if vidaMonstros > 0:
                vidaJogador -= ataqueMonstros
    
    if vidaJogador <= 0:
        return vida, municao, False, "derrotado em combate"
    elif municao <= 0:
        return vida, municao, False, "sem municao"
    else:
        return vida, municao, True, ""
            
nome = input()
vida = int(input())
partida = input()
destino = input()
armas = [["Revolver", 2, 1], ["Bastard", 3, 15], ["Duplet", 5, 2], ["VSV", 12, 3], ["Kalash", 20, 5]] # ["Nome da arma", ataque, municao gasta por ataque]
monstros = [["Lurker", 1, 2], ["Nosalis", 2 , 5], ["Spiderbug", 4, 1], ["Watcher", 5, 4], ["Librarian", 10, 20]] # ["Nome do monstro", ataque, vida]
flag = True

while flag:
    arma, municao = input().split(" com ")
    municao = municao.split(" ")
    municao = int(municao[0])
    
    proxima = input()
    
    evento = input().split()
    
    if evento[0] == "roubo":
        municao = roubo(evento[1], arma, municao)
        
    elif evento[0] == "combate":
        vida, municao, flag, motivo = combate(evento[1], evento[2], arma, municao, vida, armas, monstros)
        
    if flag == False:
        if motivo == "sem arma":
            print(f"{nome} ficou indefeso e foi devorado pelos montros! O que restou ficou no túnel para {proxima}")
        
        elif motivo == "sem municao":
            print(f"A bala faltou quando {nome} mais precisava, a caminho de {proxima}")
        
        elif motivo == "derrotado em combate":
            print(f"{nome} lutou bravamente, mas o metrô o derrotou a caminho de {proxima}")
            
    else:
        pass