# Função recursiva para saber se ganhou ou não
def ganhou(animalEsc, tabela, numeros, idx):
    for i in numeros:
        if tabela.get(animalEsc)[idx] == i[2:4]:
            return True
        
    if idx == 3:
        return False
    
    else:
        return ganhou(animalEsc, tabela, numeros, idx+1)

# Dicionario com a todos os animais e suas respectivas dezenas
tabela = {"avestruz": ["01","02","03","04"], "aguia": ["05","06","07","08"], "burro":["09","10","11","12"],
           "borboleta":["13","14","15","16"], "cachorro":["17","18","19","20"], "cabra":["21","22","23","24"],
           "carneiro":["25","26","27","28"], "camelo":["29","30","31","32"], "cobra":["33","34","35","36"],
           "coelho":["37","38","39","40"], "cavalo":["41","42","43","44"], "elefante":["45","46","47","48"],
           "galo":["49","50","51","52"], "gato":["53","54","55","56"], "jacare":["57","58","59","60"],
           "leao":["61","62","63","64"], "macaco":["65","66","67","68"], "porco":["69","70","71","72"],
           "pavao":["73","74","75","76"], "peru":["77","78","79","80"], "touro":["81","82","83","84"],
           "tigre":["85","86","87","88"], "urso":["89","90","91","92"], "veado":["93","94","95","96"],
           "vaca":["97","98","99","00"]}
numeros_escolhidos = [] # Lista com todos os números escolhidos pelo usuário

for i in range(5): # Adicionando os números na lista
    numero = input()
    numeros_escolhidos.append(numero)
    
animal_escolhido = input() # Animal escolhido pelo usuário
aposta = int(input()) # Aposta feita pelo usuário

if ganhou(animal_escolhido, tabela, numeros_escolhidos, 0): # Se for TRUE imprime uma mensagem com o valor da aposta x 18
    print(f"Parabens!!! Voce conseguiu ganhar {aposta*18} reais no jogo!!!")
else:
    print("Infelizmente nao foi dessa vez... Zeca pagodinho que acabou ganhando")