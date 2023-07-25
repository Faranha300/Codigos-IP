#Função Primo
def primo(numero, result, divisor):
    resto = numero % divisor
    
    if resto == 0:
        result += 1
    
    if divisor == 1:
        return result
    else:
        return primo(numero, result, divisor-1)

# Função Somar
def somar(numero, result, i):
    result += int(numero[i])
    
    if i == numero.index(numero[-1]):
        return result
    else:
        return somar(numero, result, i+1)

# Função Fatorial
def fatorial(numero_x, result):
    result *= numero_x
    
    if numero_x == 2:
        return result
    else:
        return fatorial(numero_x-1, result)

flag = True
acertadas = 0
erradas = 0

while flag:
    funcao = input()
    # PRIMO
    if funcao == "Primo":
        numero = int(input())
        result = 1
        if numero != 0 and numero != 1:
            result = primo(numero, result, numero//2)

        if result == 2:
            print(f"O número {numero} é primo, continue herói!")
            acertadas += 1
            erradas = 0
        else:
            print("Por aqui não.")
            erradas += 1
            acertadas = 0
    
    # SOMAR
    elif funcao == "Somar":
        numero = input()
        result = somar(numero, 0, 0)

        if result % 2 == 0:
            print(f"O número {result} é par, siga por aqui Link!")
            acertadas += 1
            erradas = 0
        else:
            print("Por aqui não.")
            erradas += 1
            acertadas = 0

    # FATORIAL
    elif funcao == "Fatorial":
        numeros = input().split()
        result = fatorial(int(numeros[0]), 1)

        if result == int(numeros[1]):
            print(f"A resposta é mesmo {result} Link, esse caminho está certo!")
            acertadas += 1
            erradas = 0
        else:
            print("Por aqui não.")
            erradas += 1
            acertadas = 0

    else:
        print("Por aqui não.")
        erradas += 1
        acertadas = 0

    # Verificação se ganhou ou perdeu
    if acertadas == 3 or erradas == 3:
        flag = False

else:
    if acertadas == 3:
        print("Com a sua ajuda o Link finalmente conseguiu sair do labirinto!!!")
    
    elif erradas == 3:
        print("Hoje não é um bom dia para o nosso herói...")