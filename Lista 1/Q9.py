vilao1 = str(input())
poder1 = int(input())
local1 = int(input()) 
vilao2 = str(input())
poder2 = int(input())
local2 = int(input())

if poder1 > 0 and poder2 > 0:
    
    destruicao1 = (poder1**2 * local1) / 2
    destruicao2 = (poder2**2 * local2) / 2
    destruicaoT = destruicao1 + destruicao2

    if destruicao1 > destruicao2:
        print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {vilao1}.")

    elif destruicao2 > destruicao1:
        print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {vilao2}.")
    
    elif destruicao1 == destruicao2:
        if destruicaoT % 2 == 0:
            print("E quem disse que isso e problema meu? Vou chamar o senhor Stark.")
    
        elif destruicaoT % 2 == 1:
            print("Vou chamar uns reforcos de outro universo... rsrs")
    
else:
    print("Nem faco essa comparacao! Quero ser um vingador, busco coisas maiores.")