X = True
jogadores = []
qtd_libero = 0
qtd_levantador = 0
qtd_ponteiro = 0
qtd_central = 0
qtd_oposto = 0

while X:
    opcao = input()
    qtd = 0
    
    if opcao == "adicionar":
        jogador = input().split(": ")
        jogadores.append(jogador)
        
        if jogadores[-1][1] == "Libero":
            qtd_libero += 1
        elif jogadores[-1][1] == "Levantador":
            qtd_levantador += 1
        elif jogadores[-1][1] == "Central":
            qtd_central += 1
        elif jogadores[-1][1] == "Ponteiro":
            qtd_ponteiro += 1
        elif jogadores[-1][1] == "Oposto":
            qtd_oposto += 1
        
        for i in range(len(jogadores)):
            if jogadores[i][1] == jogadores[-1][1]:
                qtd += 1
        
        if qtd == 5:
            if jogadores[-1][1] == "Levantador":
                print("Cuidado! voce ja possui 5 levantadores")
            elif jogadores[-1][1] == "Central":
                print("Cuidado! voce ja possui 5 centrais")
            else:
                print(f"Cuidado! voce ja possui 5 {jogadores[-1][1]}s")
        
        elif jogadores[-1][1] == "Libero" and qtd > 2:
            print("ERRO: liberos demais, nao temos uniformes suficientes")
            X = False
        
        if len(jogadores) > 18:
            print("ERRO: voce estrapolou o numero de jogadores")
            X = False
    
    elif opcao == "relatorio":
        print("No nosso time ja possuimos:")
        print(f"Liberos: {qtd_libero}")
        print(f"Levantadores: {qtd_levantador}")
        print(f"Ponteiros: {qtd_ponteiro}")
        print(f"Centrais: {qtd_central}")
        print(f"Opostos: {qtd_oposto}")
        print(f"TOTAL: {len(jogadores)}")
    
    elif opcao == "nomes":
        escolha = input()
        
        if escolha == "Libero":
            if qtd_libero == 0:
                print("Ainda nao temos jogadores nessa posicao")
            else:
                print("Os liberos sao:")
                for i in range(len(jogadores)):
                    if jogadores[i][1] == "Libero":
                        print(jogadores[i][0])
                    
        elif escolha == "Levantador":
            if qtd_levantador == 0:
                print("Ainda nao temos jogadores nessa posicao")
            else:
                print("Os levantadores sao:")
                for i in range(len(jogadores)):
                    if jogadores[i][1] == "Levantador":
                        print(jogadores[i][0])
                    
        elif escolha == "Ponteiro":
            if qtd_ponteiro == 0:
                print("Ainda nao temos jogadores nessa posicao")
            else:
                print("Os ponteiros sao:")
                for i in range(len(jogadores)):
                    if jogadores[i][1] == "Ponteiro":
                        print(jogadores[i][0])
                    
        elif escolha == "Central":
            if qtd_central == 0:
                print("Ainda nao temos jogadores nessa posicao")
            else:
                print("Os centrais sao:")
                for i in range(len(jogadores)):
                    if jogadores[i][1] == "Central":
                        print(jogadores[i][0])
                    
        elif escolha == "Oposto":
            if qtd_oposto == 0:
                print("Ainda nao temos jogadores nessa posicao")
            else:
                print("Os opostos sao:")
                for i in range(len(jogadores)):
                    if jogadores[i][1] == "Oposto":
                        print(jogadores[i][0])
    
    elif opcao == "buscar":
        nome = input()
        
        if nome == "Samuel": # Tá printando o else 18 vezes
            for i in range(len(jogadores)):
                if jogadores[i][0] == nome:
                    qtd += 1
                    
            else:
                if qtd >= 1:
                    print("Sim, Samuel, voce ja esta na lista de jogadores")
                else:
                    print("Como voce pode esquecer de si mesmo? Voce nao esta na lista")
                    
        else:
            for i in range(len(jogadores)):
                if jogadores[i][0] == nome:
                    qtd += 1
                    
            else:
                if qtd >= 1:
                    print(f"Sim, {nome} esta na lista de jogadores")
                else:
                    print(f"O jogador {nome} nao esta na lista de jogadores")
  
    elif opcao == "fim":
        X = False
        
    else:
        print("***COMANDO INVALIDO***")
        
else:
    if qtd_libero == 2 and qtd_levantador >= 2 and qtd_ponteiro >= 2 and qtd_central >= 2 and qtd_oposto >= 2 and len(jogadores) <= 18:
        print(f"O Navegantes esta pronto para disputar o Estadual! Desejem sorte aos nossos {len(jogadores)} jogadores!")
    
    else:
        print("Quem mandou ficar perdendo tempo com TikTok... Agora o Navegantes nao conseguira jogar o estadual :(")