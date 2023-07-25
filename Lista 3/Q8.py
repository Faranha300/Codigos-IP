from math import floor

N = int(input())
lifestyle = 0
utilidades = 0
dancinhas = 0
pessoas = []
views = []
M = 1000000
K = 1000

for i in range(N):
    pessoa = []
    nome, qtd_seguidores, qtd_views, categoria = input().split(", ")
    
    if "M" in qtd_seguidores:
        qtd_seguidores = qtd_seguidores.replace("M", "")
        qtd_seguidores = float(qtd_seguidores) * M

    elif "K" in qtd_seguidores:
        qtd_seguidores = qtd_seguidores.replace("K", "")
        qtd_seguidores = float(qtd_seguidores) * K
    
    if "M" in qtd_views:
        qtd_views = qtd_views.replace("M", "")
        qtd_views = float(qtd_views) * M
        
    elif "K" in qtd_views:
        qtd_views = qtd_views.replace("K", "")
        qtd_views = float(qtd_views) * K

    pessoa.append(nome)
    pessoa.append(qtd_seguidores)
    pessoa.append(categoria)
    pessoa.append(qtd_views)
    pessoas.append(pessoa)
    
    if categoria == "Lifestyle":
        lifestyle += 1
    elif categoria == "Utilidades":
        utilidades += 1
    elif categoria == "Dancinhas":
        dancinhas += 1

else:
    print("Lifestyle;")
    if lifestyle == 0:
        print("Nao foram informados dados sobre esta categoria.\n")
    else:
        print(f"Quantidade de Tiktokers: {lifestyle}")

        soma = 0
        for i in range(len(pessoas)):
            if pessoas[i][2] == "Lifestyle":
                soma += pessoas[i][1]

        media_seg = soma / lifestyle
        media_seg = media_seg / 1000000
        media_seg = floor(media_seg * 10) / 10

        print(f"Media de seguidores: {media_seg:.1f}M")
        pessoas_sort = []
        for i in range(len(pessoas)):
            if pessoas[i][2] == "Lifestyle":
                pessoas_sort.append(pessoas[i][3])
        pessoas_sort.sort(reverse=True)
        Max_view = pessoas_sort[0] / 1000000
        print(f"Maximo de visualizações: {Max_view:.2f}M\n")
    
    print("Utilidades;")
    if utilidades == 0:
        print("Nao foram informados dados sobre esta categoria.\n")
    else:
        print(f"Quantidade de Tiktokers: {utilidades}")

        soma = 0
        for i in range(len(pessoas)):
            if pessoas[i][2] == "Utilidades":
                soma += pessoas[i][1]

        media_seg = soma / utilidades
        media_seg = media_seg / 1000000
        media_seg = floor(media_seg * 10) / 10

        print(f"Media de seguidores: {media_seg:.1f}M")
        pessoas_sort = []
        for i in range(len(pessoas)):
            if pessoas[i][2] == "Utilidades":
                pessoas_sort.append(pessoas[i][3])
        pessoas_sort.sort(reverse=True)
        Max_view = pessoas_sort[0] / 1000000
        print(f"Maximo de visualizações: {Max_view:.2f}M\n")
        
    print("Dancinhas;")
    if dancinhas == 0:
        print("Nao foram informados dados sobre esta categoria.\n")
    else:
        print(f"Quantidade de Tiktokers: {dancinhas}")
        
        soma = 0
        for i in range(len(pessoas)):
            if pessoas[i][2] == "Dancinhas":
                soma += pessoas[i][1]
        media_seg = soma / dancinhas
        media_seg = media_seg / 1000000
        media_seg = floor(media_seg * 10) / 10

        print(f"Media de seguidores: {media_seg:.1f}M")
        pessoas_sort = []
        for i in range(len(pessoas)):
            if pessoas[i][2] == "Dancinhas":
                pessoas_sort.append(pessoas[i][3])
        pessoas_sort.sort(reverse=True)
        Max_view = pessoas_sort[0] / 1000000
        print(f"Maximo de visualizações: {Max_view:.2f}M\n")

    X = len(pessoas) - 1
    melhor = pessoas[-1][0]
    maior_seg = pessoas[-1][1]
    melhor_categ = pessoas[-1][2]
    for i in range(X):
        if maior_seg < pessoas[i][1]:
            melhor = pessoas[i][0]
            maior_seg = pessoas[i][1]
            melhor_categ = pessoas[i][2]

    if maior_seg > 1000000:
        maior_seg = str(maior_seg / 1000000) + "M"

    elif maior_seg > 1000:
        maior_seg = str(maior_seg / 1000) + "K"

    print(f"Os olhares do mundo estao sobre {melhor.upper()}, que conta com {maior_seg} de seguidores vendo seus videos diarios de {melhor_categ}!")