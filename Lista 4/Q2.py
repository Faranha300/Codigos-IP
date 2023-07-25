def palindromo(frase):
    frase = frase.replace(" ", "")
    frase_reverse = frase[::-1]
    if frase == frase_reverse:
        return True
    
def pangrama(frase):
    alfabeto = "abcdefghijlmnopqrstuvxz"
    count = 0
    for i in alfabeto:
        if i in frase:
            count += 1
                
    if count == 23:
        return True

def epizeuxe(frase):
    palavras = frase.split()
    count = 0
    
    for i in palavras:
        for j in range(len(palavras)):
            if i == palavras[j]:
                count += 1
    
    if count >= len(palavras) + 2:
        return True

N = int(input())
lista = []

for i in range(N):
    frase = str(input())
    
    lista.append(frase)
    
for i in range(len(lista)):
    if palindromo(lista[i]):
        print(f'Freddy, "{lista[i]}" é um palíndromo!')

    elif pangrama(lista[i]):
        print(f'Tenho certeza de que "{lista[i]}" é um pangrama!')
        
    elif epizeuxe(lista[i]):
        print(f'Freddy, Freddy, "{lista[i]}" é definitivamente uma epizeuxe!')
        
    else:
        print("Essa aqui é uma pegadinha, não há nada aqui!")