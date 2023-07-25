N = int(input())
NI = N

while N > 0:
    pessoa = input()
    
    if pessoa == "Prior":
        print("IIIHHH! El mago esta eliminado!")
    elif pessoa == "Manu":
        print("Manu saiu! Bruna Marquezine deve estar muito triste :(")
    elif pessoa == "Pyong":
        print("Agora o Pyong que dormiu, esta eliminado")
    elif pessoa == "Gizelly":
        print("PPPPPYYYYYOOOONNNGGG LEEEEEE, Gizelly volta pra casa!")
    
    if NI == N:
        paredao = pessoa
        
    elif N == 1:
        lider = pessoa
        
    N -= 1
        
else:
    print(f"- O indicado(a) ao paredao nessa semana e: {paredao}")
    
    if NI == 19:
        print(f"- O novo lider da semana e: {lider}!")
        
    else:
        NI = 19 - NI
        print(f"- Ainda restam {NI} pessoas na disputa pela lideranca!")