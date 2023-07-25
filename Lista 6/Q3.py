# Nome do produto: [quantidade, preco, resgatados]
tabela = {"bichinho de pelucia": [10,750,0],
          "boneco articulado com armadura": [20,1000,0],
          "estatua de cena memoravel": [10,1250,0],
          "camiseta tematica": [10,500,0],
          "chaveiro": [50,250,0],
          "bolinhas": [10000,1000,0]}
flag = True
bolinhas = 0
ienes = 0
qtdVendas = 0
qtdResgates = 0
bolinhasGastas = 0

while flag:
    comando = input()
    
    if comando == "comprar":
        valor = int(input())
        if tabela.get("bolinhas")[0] > 0:
            if valor > tabela.get("bolinhas")[0]:
                valor = tabela.get("bolinhas")[0]
            tabela.update({"bolinhas": [tabela.get("bolinhas")[0] - valor, 1000, tabela.get("bolinhas")[2] + valor]})
            bolinhas += valor
            qtdVendas += 1
            ienes += valor*1000
            print(f"O jogador comprou {valor} bolinhas por {valor*1000} ienes.")
            
        else:
            print("Nao ha mais bolinhas disponiveis, melhor esperar um pouco.")
    
    elif comando == "trocar":
        nome, valor = input().split(" - ")
        valor = int(valor)
        
        if nome in tabela:
            if tabela.get(nome)[0] > 0:
                if valor >= tabela.get(nome)[1]:
                    bolinhas -= tabela.get(nome)[1]
                    tabela.update({nome: [tabela.get(nome)[0]-1, tabela.get(nome)[1], tabela.get(nome)[2]+1]})
                    qtdResgates += 1
                    bolinhasGastas += tabela.get(nome)[1]
                    print(f"O jogador trocou {tabela.get(nome)[1]} bolinhas por um {nome}.")
                else:
                    print(f"O jogador precisa de mais {tabela.get(nome)[1]-valor} bolinhas para trocar por um {nome}.")
            else:
                print(f"O jogador veio trocar suas bolinhas mas o premio {nome} nao esta disponivel.")
        else:
            print(f"O jogador veio trocar suas bolinhas mas o premio {nome} nao esta disponivel.")
    
    elif comando == "hora de fechar": # Resumo do dia
        premiosRestantes = tabela.get('bichinho de pelucia')[0] + tabela.get('boneco articulado com armadura')[0] + tabela.get('estatua de cena memoravel')[0] + tabela.get('camiseta tematica')[0] + tabela.get('chaveiro')[0]
        print("\nO resumo do dia foi:")
        print(f"Arrecadado: {ienes} ienes em {qtdVendas} vendas;")
        print(f"Bolinhas: {tabela.get('bolinhas')[0] + bolinhasGastas} restantes;")
        print(f"Resgates feitos: {qtdResgates};")
        print(f"Bolinhas recebidas: {bolinhasGastas};")
        print(f"Premios: {premiosRestantes} restantes;")
        print("Deu a hora, amanha tem mais!")
        flag = False