def calcula(velocidade, KM, moedas):
    velocidade += KM
    moedas -= 1
    
    if moedas == 0:
        return velocidade
    else:
        return calcula(velocidade, KM, moedas)
    
nome = input()
velocidade = int(input())
pista = input()
moedas = int(input())

if pista == "Mario Kart Stadium":
    KM = 3
elif pista == "Bowsers Castle":
    KM = 4
elif pista == "Moo Moo Meadows":
    KM = 5
elif pista == "Yoshi Valley":
    KM = 6
elif pista == "Rainbow Road":
    KM = 7

velocidade = calcula(velocidade, KM, moedas)

print(f"Correndo na pista {pista}, {nome} coletou {moedas} moedas e terminou a corrida na incrivel velocidade de {velocidade} km/h.")