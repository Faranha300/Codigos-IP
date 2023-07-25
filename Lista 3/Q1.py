N = int(input())
meninos = []
meninas = []

while N > 0:
    nome, genero = str(input()).split(" - ")

    if genero == "M":
        meninos.append(nome)

    else:
        meninas.append(nome)

    N -= 1

else:
    if len(meninas) == 0:
        print(", ".join(meninos) + ", Querem cafe?")
        print(f"Serao necessarias {len(meninos)} porcoes de cafe")

    elif len(meninos) == 0:
        print(", ".join(meninas) + ", Desculpa, so pros meninos HAHAHAHAAHHAHAHA")
        print("Nao tem meninos na lista, nao precisa fazer cafe, Neuma")

    else:
        print(", ".join(meninos) + ", Querem cafe?")
        print(", ".join(meninas) + ", Desculpa, so pros meninos HAHAHAHAAHHAHAHA")
        print(f"Serao necessarias {len(meninos)} porcoes de cafe")