acidez = 20
agua = 15
tempero = 10

while (acidez != agua or acidez != tempero or agua != tempero):
    N = int(input())
    acao = input()
    
    if acao == "reduzir agua":
        agua -= N
        tempero += (N-1)
    elif acao == "adicionar agua":
        agua += N
        tempero -= (N+2)
    elif acao == "reduzir acidez":
        acidez -= N
    elif acao == "aumentar acidez":
        acidez += N
    elif acao == "aumentar tempero":
        tempero += N
    
    if acidez != agua or acidez != tempero or agua != tempero:
        if agua < acidez and agua < tempero:
            print("Muit seca! melhorre a combinaçon")
        elif tempero < agua and tempero < acidez:
            print("Falta tomperro! non agradou meu paladar")
        elif acidez < agua and acidez < tempero:
            print("Falta acidez! non pode subir o mezanin")
        elif agua < acidez and agua == tempero:
            print("Muit seca! melhorre a combinaçon")
            print("Falta tomperro! non agradou meu paladar")
        elif agua < tempero and agua == acidez:
            print("Muit seca! melhorre a combinaçon")
            print("Falta acidez! non pode subir o mezanin")
        elif acidez < agua and acidez == tempero:
            print("Falta tomperro! non agradou meu paladar")
            print("Falta acidez! non pode subir o mezanin")
            
else:
    print("Tem sabor, tem apresentacion, tem tudibon! sobe no mezanin")