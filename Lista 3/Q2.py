N = int(input())
usuarios = []
likes = []
likes_sort = []

while N > 0:
    usuario = str(input())
    qtd_likes = int(input())

    usuarios.append(usuario)
    likes.append(str(qtd_likes))
    
    for i, j in enumerate(likes_sort):
        if qtd_likes > int(j):
            likes_sort.insert(i, str(qtd_likes))
            break
    
    else:
        likes_sort.append(str(qtd_likes))

    N -= 1

else:
    print("O numero de curtidas dos videos que vao aparecer na For You segue a ordem:")
    print(", ".join(likes_sort))
    for i in likes:
        if i == likes_sort[0]:
            index = likes.index(i)
            pessoa_ganha = usuarios[index]
    print(f"O primeiro usuario que vai aparecer na For You e {pessoa_ganha}!")