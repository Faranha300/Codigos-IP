N = int(input()) # Máximo de rodadas!
jogador_1 = str(input())
jogador_2 = str(input())
jogador_3 = str(input())
pont_1 = 0
pont_2 = 0
pont_3 = 0

# Primeira etapa
while N > 0:
    jogada_1 = int(input())
    jogada_2 = int(input())
    jogada_3 = int(input())
    
    pont_1 += jogada_1
    pont_2 += jogada_2
    pont_3 += jogada_3
    
    if pont_1 >= 200 or pont_2 >= 200 or pont_3 >= 200 or N == 1:# Se chegar na ultima rodada da primeira etapa ou quando uma das pont for >= 200
        if pont_1 < pont_2 and pont_1 < pont_3:
            print(f"{jogador_1} ja esta confirmado no paredao")
            paredao1 = jogador_1
            
            if pont_2 > pont_3:
                print(f"1° - {jogador_2}")
                print(f"2° - {jogador_3}")
                
                N = int(input())# Segunda etapa
                pont_1 = 0
                pont_2 = 0
                while N > 0:
                    jogada_1 = int(input())
                    jogada_2 = int(input())
    
                    pont_1 += jogada_1
                    pont_2 += jogada_2
    
                    N -= 1
                    
                else:
                    if pont_1 > pont_2:
                        print(f"Nosso paredao sera entre {jogador_3} e {paredao1}")
                    else:
                        print(f"Nosso paredao sera entre {jogador_2} e {paredao1}")
                    
            else:
                print(f"1° - {jogador_3}")
                print(f"2° - {jogador_2}")
                
                N = int(input())# Segunda etapa
                pont_1 = 0
                pont_2 = 0
                while N > 0:
                    jogada_1 = int(input())
                    jogada_2 = int(input())
    
                    pont_1 += jogada_1
                    pont_2 += jogada_2
    
                    N -= 1
                    
                else:
                    if pont_1 > pont_2:
                        print(f"Nosso paredao sera entre {jogador_2} e {paredao1}")
                    else:
                        print(f"Nosso paredao sera entre {jogador_3} e {paredao1}")

        elif pont_2 < pont_1 and pont_2 < pont_3:
            print(f"{jogador_2} ja esta confirmado no paredao")
            paredao1 = jogador_2
            
            if pont_1 > pont_3:
                print(f"1° - {jogador_1}")
                print(f"2° - {jogador_3}")
                
                N = int(input())# Segunda etapa
                pont_1 = 0
                pont_2 = 0
                while N > 0:
                    jogada_1 = int(input())
                    jogada_2 = int(input())
    
                    pont_1 += jogada_1
                    pont_2 += jogada_2
    
                    N -= 1
                    
                else:
                    if pont_1 > pont_2:
                        print(f"Nosso paredao sera entre {jogador_3} e {paredao1}")
                    else:
                        print(f"Nosso paredao sera entre {jogador_1} e {paredao1}")
                        
            else:
                print(f"1° - {jogador_3}")
                print(f"2° - {jogador_1}")

                N = int(input())# Segunda etapa
                pont_1 = 0
                pont_2 = 0
                while N > 0:
                    jogada_1 = int(input())
                    jogada_2 = int(input())
    
                    pont_1 += jogada_1
                    pont_2 += jogada_2
    
                    N -= 1
                    
                else:
                    if pont_1 > pont_2:
                        print(f"Nosso paredao sera entre {jogador_1} e {paredao1}")
                    else:
                        print(f"Nosso paredao sera entre {jogador_3} e {paredao1}")
            
        elif pont_3 < pont_1 and pont_3 < pont_2:
            print(f"{jogador_3} ja esta confirmado no paredao")
            paredao1 = jogador_3
            
            if pont_1 > pont_2:
                print(f"1° - {jogador_1}")
                print(f"2° - {jogador_2}")
                
                N = int(input())# Segunda etapa
                pont_1 = 0
                pont_2 = 0
                while N > 0:
                    jogada_1 = int(input())
                    jogada_2 = int(input())
    
                    pont_1 += jogada_1
                    pont_2 += jogada_2
    
                    N -= 1
                    
                else:
                    if pont_1 > pont_2:
                        print(f"Nosso paredao sera entre {jogador_2} e {paredao1}")
                    else:
                        print(f"Nosso paredao sera entre {jogador_1} e {paredao1}")
                        
            else:
                print(f"1° - {jogador_2}")
                print(f"2° - {jogador_1}")
                
                N = int(input())# Segunda etapa
                pont_1 = 0
                pont_2 = 0
                while N > 0:
                    jogada_1 = int(input())
                    jogada_2 = int(input())
    
                    pont_1 += jogada_1
                    pont_2 += jogada_2
    
                    N -= 1
                    
                else:
                    if pont_1 > pont_2:
                        print(f"Nosso paredao sera entre {jogador_1} e {paredao1}")
                    else:
                        print(f"Nosso paredao sera entre {jogador_2} e {paredao1}")
                
    N -= 1