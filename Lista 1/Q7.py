escolha = int(input())

if escolha >= 1 and escolha <= 6:
    if escolha == 1:
        print("A arma corpo a corpo escolhida foi: Cassetete")

    elif escolha == 2:
        print("A arma corpo a corpo escolhida foi: Garrafa de Whisky")

    elif escolha == 3:
        print("A arma corpo a corpo escolhida foi: Soco Ingles")

    elif escolha == 4:
        print("A arma corpo a corpo escolhida foi: Lamina Escondida")

    elif escolha == 5:
        print("A arma corpo a corpo escolhida foi: Pe de Cabra")

    elif escolha == 6:
        print("A arma corpo a corpo escolhida foi: Canivete")

    if escolha % 2 == 1:
        print("A arma corpo a corpo escolhida e atordoante")

    else:
        print("A arma corpo a corpo escolhida e cortante")

else:
    print("Numero invalido")