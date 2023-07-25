N = int(input())
nomes_ord = []
seguidores_ord = []

for i in range(N):
    nome, qtd_seguidores = input().split("-")

    for i, j in enumerate(seguidores_ord):
        if int(qtd_seguidores) < int(j):
            seguidores_ord.insert(i , str(qtd_seguidores))
            nomes_ord.insert(i, nome)
            break

    else:
        seguidores_ord.append(str(qtd_seguidores))
        nomes_ord.append(nome)

else:
    for i in range(len(nomes_ord)):
        print(nomes_ord[i] + "-" + seguidores_ord[i])