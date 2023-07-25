def palindromo(pista, cont):
    pista_reverse = pista[::-1]
    cont += 1

    if pista_reverse == pista:
        return True
    elif cont >= 995:
        return False
    else:
        return palindromo("a" + pista, cont)

N = int(input())
cont = 0
defcont = 0

for i in range(N):
    pista = input()
    result = palindromo(pista, defcont)

    if result == True:
        cont += 1
        
else:
    if cont == N:
        print("ACHEI!!! Peach, estou a caminho.")
    else:
        print("Essa não!!! Estou na direção errada.")