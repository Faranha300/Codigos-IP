ruidos = ["tss", "zzz"]
musica = []
qtd_ruidos = 0

for i in range(10):
    trecho = input()
    X = True
    
    if trecho in ruidos:
        qtd_ruidos += 1

    else: # tá tirando 2 ruidos e tá somando só 1 doq 2
        while X:
            if ruidos[0] + " " in trecho:
                trecho = trecho.replace(ruidos[0] + " ", "", 1)
                qtd_ruidos += 1
            elif ruidos[1] + " " in trecho:
                trecho = trecho.replace(ruidos[1] + " ", "", 1)
                qtd_ruidos += 1
            elif " " + ruidos[0] in trecho:
                trecho = trecho.replace(" " + ruidos[0], "", 1)
                qtd_ruidos += 1
            elif " " + ruidos[1] in trecho:
                trecho = trecho.replace(" " + ruidos[1], "", 1)
                qtd_ruidos += 1
            else:
                X = False
        else:
            musica.append(trecho)

else:
    if len(musica) == 0:
        print("Eita, a legenda simplesmente inexiste! Tudo era ruido!")
    
    else:
        print("Legenda final:\n")

        for i in musica:
            print(i)

        if len(musica) >= 8 and qtd_ruidos <= 4:
            if qtd_ruidos > 1 and qtd_ruidos < 5:
                print("\nTodo o ruido foi removido e voce mandou bem! A legenda saiu certinha. Pode subir!")

            elif qtd_ruidos == 0:
                print("\nNem precisava rodar, o audio ja estava limpinho e a legenda ta nos conformes. Marca o @billyraycyrus")

        else:
            print("\nIh, tem alguma coisa errada com a legenda, ta estranha. Melhor dar uma verificada e regravar.")