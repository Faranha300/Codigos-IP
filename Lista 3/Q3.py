X = 3
a = []
b = []
c = []

while X > 0:
    nome = str(input())
    qtd_views1 = int(input())
    qtd_views2 = int(input())

    media = int((qtd_views1 + qtd_views2) / 2)

    if X == 3:
        a.append(nome)
        a.append(media)

    elif X == 2:
        b.append(nome)
        b.append(media)

    else:
        c.append(nome)
        c.append(media)

    X -= 1

else:
    if a[1] > b[1] and a[1] > c[1]:
        print(f"1º Lugar: {a[0]} com a media de views: {a[1]}")
        if b[1] > c[1]:
            print(f"2º Lugar: {b[0]} com a media de views: {b[1]}")
            print(f"3º Lugar: {c[0]} com a media de views: {c[1]}")
        else:
            print(f"2º Lugar: {c[0]} com a media de views: {c[1]}")
            print(f"3º Lugar: {b[0]} com a media de views: {b[1]}")

    elif b[1] > a[1] and b[1] > c[1]:
        print(f"1º Lugar: {b[0]} com a media de views: {b[1]}")
        if a[1] > c[1]:
            print(f"2º Lugar: {a[0]} com a media de views: {a[1]}")
            print(f"3º Lugar: {c[0]} com a media de views: {c[1]}")
        else:
            print(f"2º Lugar: {c[0]} com a media de views: {c[1]}")
            print(f"3º Lugar: {a[0]} com a media de views: {a[1]}")

    elif c[1] > a[1] and c[1] > b[1]:
        print(f"1º Lugar: {c[0]} com a media de views: {c[1]}")
        if a[1] > b[1]:
            print(f"2º Lugar: {a[0]} com a media de views: {a[1]}")
            print(f"3º Lugar: {b[0]} com a media de views: {b[1]}")
        
        else:
            print(f"2º Lugar: {b[0]} com a media de views: {b[1]}")
            print(f"3º Lugar: {a[0]} com a media de views: {a[1]}")