Nome1, N1, Dura1 = input().split("-")
Nome2, N2, Dura2 = input().split("-")
Nome3, N3, Dura3 = input().split("-")

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
Dura1 = int(Dura1)
Dura2 = int(Dura2)
Dura3 = int(Dura3)

if N1 or N2 or N3 >= 4.0:
    if N1 > N2 and N1 > N3:
        print(Nome1)

    elif N2 > N1 and N2 > N3:
        print(Nome2)

    elif N3 > N1 and N3 > N2:
        print(Nome3)

    elif N1 == N2:

        if Dura1 < Dura2:
            print(Nome1)
        else:
            print(Nome2)

    elif N1 == N3:

        if Dura1 < Dura3:
            print(Nome1)
        else:
            print(Nome3)

    elif N2 == N3:

        if Dura2 < Dura3:
            print(Nome2)
        else:
            print(Nome3)

else:
    print("Nota minima nao atingida")
