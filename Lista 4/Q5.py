def descobrir_index_1P(pessoa, pessoas):
    for i in range(len(pessoas)):
        if pessoas[i][0] == pessoa:
            idx = i

    return idx

def parte_dinamica1(pessoa, relacionamentos, pessoas):
    soma = 0
    for i in relacionamentos[pessoa]:
        if relacionamentos[pessoa] != -1:
            soma += i

    media = soma / 6
    if media > 5:
        print(f"UFA!!! foi por pouco mas {pessoas[pessoa][0]} conseguiu escapar do Wendigo.")
        return True
    
    else:
        print(f"{pessoas[pessoa][0]} infelizmente nao conseguiu sobreviver ao ataque do Wendigo.")
        return False

def descobrir_index(nome1, nome2, pessoas):

    for i in range(len(pessoas)):
        if pessoas[i][0] == nome1:
            idx1 = i
    for i in range(len(pessoas)):
        if pessoas[i][0] == nome2:
            idx2 = i

    return idx1, idx2

def parte_dinamica2(pessoa1, pessoa2, relacionamentos, pessoas):
    if relacionamentos[pessoa1][pessoa2] > 6:
        print(f"felizmente {pessoas[pessoa2][0]} ajudou {pessoas[pessoa1][0]} a escapar do Wendigo.")
        return True
    else:
        print(f"que pena! {pessoas[pessoa2][0]} nao conseguiu ajudar {pessoas[pessoa1][0]} do ataque do Wendigo.")
        return False

def interacao_inicial(pessoa1, interacao, pessoa2, relacionamentos):

    if interacao == "O":
        relacionamentos[pessoa1][pessoa2] += 1
        relacionamentos[pessoa2][pessoa1] += 1
    elif interacao == "X":
        relacionamentos[pessoa1][pessoa2] -= 1
        relacionamentos[pessoa2][pessoa1] -= 1

pessoas = [["Sam", "vivo"], ["Chris", "vivo"], ["Ashley", "vivo"], ["Jessica", "vivo"], ["Mike", "vivo"], ["Emily", "vivo"], ["Matt", "vivo"]]
relacionamentos = [[-1,5,5,5,5,5,5],[5,-1,6,5,5,5,5],[5,6,-1,5,5,5,5],[5,5,5,-1,7,4,5],[5,5,5,7,-1,3,4],[5,5,5,4,3,-1,7],[5,5,5,5,4,7,-1]]
pessoas_vivas = []
N = int(input())

for i in range (N): # 1 Rodada
    nome1, interacao, nome2 = input().split()

    idx1, idx2 = descobrir_index(nome1, nome2, pessoas)
    interacao_inicial(idx1, interacao, idx2, relacionamentos)

N = int(input())

for i in range(N): # 2 Rodada
    acontecimento = input().split(" - ")

    if len(acontecimento) == 1: # se for dado somente 1 pessoa
        idx = descobrir_index_1P(acontecimento[0], pessoas)
        if pessoas[idx][1] == "morto":
            print("entrada invalida!!! voce so pode jogar com jogadores vivos")
        else:
            if not parte_dinamica1(idx, relacionamentos, pessoas):
                pessoas[idx][1] = "morto"
    
    elif len(acontecimento) == 2: # se for dado 2 pessoas
        idx1, idx2 = descobrir_index(acontecimento[0], acontecimento[1], pessoas)
        if pessoas[idx1][1] == "morto":
            print("entrada invalida!!! voce so pode jogar com jogadores vivos")
        elif pessoas[idx2][1] == "morto":
            print("entrada invalida!!! voce so pode jogar com jogadores vivos")
        else:
            if not parte_dinamica2(idx1, idx2, relacionamentos, pessoas):
                pessoas[idx1][1] = "morto"

print()

for i in range(len(pessoas)):
    if pessoas[i][1] == "vivo":
        pessoas_vivas.append(pessoas[i][0])

if len(pessoas_vivas) > 0:
    print("Sobreviventes:")
    for i in pessoas_vivas:
        print(i)

else:
    print("Tristemente, ninguém sobreviveu")