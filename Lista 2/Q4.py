N = int(input())
nomeP = ""
mediaB = 11

while N > 0:
    nome = input()
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    
    media = (nota1 + nota2 + nota3) / 3

    if mediaB > media:
        nomeP = nome
        mediaB = media

    N -= 1

else:
    if mediaB <= 0:
        print("Ocorreu um erro no sistema de notas, por favor insira notas validas")
    
    else:
        print(f"O chef eliminado da vez é: {nomeP} - {mediaB:.2f}")