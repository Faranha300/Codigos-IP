X = True
lista = []

while X:
    opcao = str(input())

    if opcao == "adicionar":
        nome, posicao = str(input()).split(" ")
        lista.insert(int(posicao), nome)

    elif opcao == "remover":
        nome = str(input())
        lista.remove(nome)

    elif opcao == "atualizar indice":
        nome, posicao = str(input()).split(" ")
        
        posicao_antiga = lista.index(nome)
        
        lista.remove(nome)
        lista.insert(int(posicao), nome)

        if posicao_antiga == int(posicao):
            print("Nada mudou, a lista permanece igual")

    elif opcao == "imprimir lista atual":
        print(" ".join(lista))

    elif opcao == "lista finalizada":
        X = False
        print("A lista ficou da seguinte forma:")
        print(" ".join(lista))

    else:
        print("Opçao não encontrada")