N = int(input())
maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lista = []

while N > 0:
    X = False
    hashtag = str(input())
    
    for i in hashtag:
        for j in maiuscula:
            if i == j:
                X = True
                
    if X == False:
        for i, j in enumerate(lista):
            if hashtag < j:
                lista.insert(i, hashtag)
                break
        else:
            lista.append(hashtag)

    N -= 1

else:
    for i in lista:
        print(i)