cartas = {'As': 1,'2': 2, '3': 3, '4': 4, '5': 5,
          '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
          'Valete': 11, 'Dama': 11, 'Rei': 11}
naipes = ("ouros", "paus", "espadas", "copas")
# posicao da carta: (numero da carta, naipe)
cartas_jogadas = {}
idxCarta = 0
pontuacao_jogador = 0
pontuacao_casa = 0

while pontuacao_jogador < 17: # Vez do Jogador
    carta = input()
    carta_split = carta.split(" ")
    if len(carta_split) == 3:
        if carta_split[0] in cartas:
            if carta_split[2] in naipes:
                naipe = carta_split[2]
                carta = carta_split[0]
                encontrou = False
                for i in cartas_jogadas:
                    if carta == cartas_jogadas.get(i)[0] and naipe == cartas_jogadas.get(i)[1]:
                        encontrou = True
                
                if not encontrou:
                    cartas_jogadas.update({idxCarta: (carta, naipe)})
                    idxCarta += 1
                    pontuacao_jogador += cartas.get(carta)
                
                else:
                    print("EIEIEI, QUE ROUBO É ESSE!!!")
            else:
                print(f"A carta {carta} não existe, não me enganarão!")
        else:
            print(f"A carta {carta} não existe, não me enganarão!")
    
    else:
        print(f"A carta {carta} não existe, não me enganarão!")

print(f"Minha rodada acaba por aqui com {pontuacao_jogador} pontos.")
if pontuacao_jogador == 21:
    print("Blackjack!")
elif pontuacao_jogador > 21:
    print("Ah não, passei do ponto!")

if not pontuacao_jogador > 21:
    while pontuacao_casa < 17: # Vez do Dealer
        carta = input()
        carta_split = carta.split(" ")
        if len(carta_split) == 3:
            if carta_split[0] in cartas:
                if carta_split[2] in naipes:
                    naipe = carta_split[2]
                    carta = carta_split[0]
                    encontrou = False
                    for i in cartas_jogadas:
                        if carta == cartas_jogadas.get(i)[0] and naipe == cartas_jogadas.get(i)[1]:
                            encontrou = True
                            
                    if not encontrou:
                        cartas_jogadas.update({idxCarta: (carta, naipe)})
                        idxCarta +=1
                        pontuacao_casa += cartas.get(carta)
                    
                    else:
                        print("EIEIEI, QUE ROUBO É ESSE!!!")
                else:
                    print(f"A carta {carta} não existe, não me enganarão!")
            else:
                print(f"A carta {carta} não existe, não me enganarão!")
                
        else:
            print(f"A carta {carta} não existe, não me enganarão!")

    print(f"A rodada da casa acaba por aqui com {pontuacao_casa} pontos.")
    if pontuacao_casa == 21:
        print("Blackjack!")
    elif pontuacao_casa > 21:
        print("AEEEEEEE, ele passou de 21, poder ir pagando chefa!!")

# Resultado Final 
if not pontuacao_jogador > 21 and not pontuacao_casa > 21:
    if pontuacao_jogador > pontuacao_casa:
        print("O dinheiro é meu!")
        
    elif pontuacao_casa > pontuacao_jogador:
        print("Perdi tudo, F.")

    elif pontuacao_jogador == pontuacao_casa:
        print("A próxima eu levo.")