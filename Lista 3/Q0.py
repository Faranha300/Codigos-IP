lista = []
passo = str

while passo != "FIM":
    passo = str(input())
    
    lista.append(passo)
    
else:
    print(f"Olá seguimores! O primeiro passo da dancinha é {lista[0]}")
    print(f"Depois, a gente faz o {lista[1]} e {lista[2]}")
    print(f"Temos ainda mais {len(lista) - 4} passos pra aprender!")
    print(f"Por último, vamos fazer o {lista[-2]}")