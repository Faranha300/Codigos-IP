def vencedor(cartaLuke, cartaAdv):
    if cartaLuke > cartaAdv:
        return True

baralhoLuke = []
baralhoAdv = []
vitorias1 = 0
vitorias2 = 0
round = 1
X = True

for i in range(10):
    carta = input().split("/")
    
    if i >= 0 and i < 5:
        baralhoLuke.append(carta)
        
    elif i >= 5 and i < 10:
        baralhoAdv.append(carta)

while X:
    if vencedor(int(baralhoLuke[round - 1][1]), int(baralhoAdv[round - 1][1])):
        print(f"Luke foi muito esperto, usou {baralhoLuke[round - 1][0]} e ganhou o {round}º round!")
        vitorias1 += 1
    else:
        print(f"Inscryption nao aliviou, usou {baralhoAdv[round - 1][0]} e venceu o {round}º round!")
        vitorias2 += 1
        
    round += 1
        
    if vitorias1 == 3 or vitorias2 == 3:
        X = False
        
else:
    if vitorias1 > vitorias2:
        print("Luke Carter ganhou na batalha de cartas e avançou de fase na sua luta para conseguir sair da cabana!")
    else:
        print("Luke Carter foi derrotado na batalha de cartas e sua alma permanecera na cabana para todo o sempre!")        