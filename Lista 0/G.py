flag = True

while flag:
    D = int(input())
    if D <= 1:
        print("Numero invalido")
    else:
        flag = False
    
if D <= 10:
    P = "Arthur"
    print(P)

elif D <= 30:
    P = "Luiz"
    print(P)

elif D <= 100:
    P = "Pedro"
    print(P)

else:
    P= "Nenhum"
    print(P)