# Função para criar o nome shipado e se conseguir adiciona 20 aos pontos
def shipador(nome1, nome2, pontos):
    nomeNovo = ""
    nome1 = list(nome1)
    nome2 = list(nome2)
    contador = 0
    
    for i in nome1:
        for j in nome2:
            if i == j and contador != 1:
                idx1 = nome1.index(i)
                idx2 = nome2.index(j)
                contador = 1
                
    if contador == 0: # Quando os nomes não tiverem letras em comum
        nomeNovoList = nome1[:len(nome1)//2] + nome2[len(nome2)//2:]
        for i in nomeNovoList:
            nomeNovo += i
    
    else:       
        nomeNovoList = nome1[:idx1] + nome2[idx2:]
        pontos += 20
        for i in nomeNovoList:
            nomeNovo += i
        
    return nomeNovo, pontos

# Função para calcular quantos pontos as duas pessoas vão ter
def calcularPontos(caracteristicasP1, caracteristicasP2, pontos):
    for i in caracteristicasP1:
        if i == "Azeitona":
            if caracteristicasP1.get(i) != caracteristicasP2.get(i):
                pontos += 50
                
        elif i == "Series" or i == "Filmes" or i == "Musicas" or i == "Livros":
            for j in caracteristicasP1.get(i):
                for k in caracteristicasP2.get(i):
                    if j == k:
                        pontos += 2
        
        elif i == "Aniversario":
            if caracteristicasP1.get(i)[0] == caracteristicasP2.get(i)[0]:
                pontos += 10            
            elif caracteristicasP1.get(i)[1] == "ar" and caracteristicasP2.get(i)[1] == "agua" or caracteristicasP1.get(i)[1] == "agua" and caracteristicasP2.get(i)[1] == "ar":
                pontos += 5
            elif caracteristicasP1.get(i)[1] == "fogo" and caracteristicasP2.get(i)[1] == "terra" or caracteristicasP1.get(i)[1] == "terra" and caracteristicasP2.get(i)[1] == "fogo":
                pontos += 5
        
        else:
            if caracteristicasP1.get(i) == caracteristicasP2.get(i):
                pontos += 3
        
    return pontos

# Função para saber qual o signo da pessoa e seu elemento
def descobrirSigno(aniversario, signos, elementos):
    numero = aniversario.split("/")
    
    numero = int(numero[1])
    signo = signos.get(numero)
    
    for i in elementos.keys():
        for j in elementos.get(i):
            if signo == j:
                elemento = i
    
    return signo, elemento

signos = {4 :"aries", 5 :"touro", 6 :"gemeos", 7 :"cancer",
          8 :"leao", 9 :"virgem", 10 :"libra", 11 :"escorpiao",
          12 :"sagitario", 1 :"capricornio", 2 :"aquario", 
          3 :"peixes"}
elementos = {"agua": ("cancer", "peixes", "escorpião"), "fogo": ("aries", "leao", "Sagitario"),
             "terra": ("touro", "virgem", "capricornio"), "ar": ("gemeos", "libra", "aquario")}

# caracteristica: (gosto(s))
caracteristicasP1 = {}
caracteristicasP2 = {}
flag = True
pontos = 0

print("Digite seu nome e o nome do/da Crush:")
nome1 = input()
nome2 = input()

while flag: # Caracteristicas da Pessoa 1
    caracteristica = input("").split()
    
    # Se a caracteristica for Musica|Filme|Serie|Livro
    if caracteristica[0] == "Musicas" or caracteristica[0] == "Filmes" or caracteristica[0] == "Series" or caracteristica[0] == "Livros":
        gostos = caracteristica
        caracteristica = gostos.pop(0)
        caracteristicasP1.update({caracteristica: gostos})
        
    # Se a caracteristica for Aniversario
    elif caracteristica[0] == "Aniversario":
        signo, elemento = descobrirSigno(caracteristica[1], signos, elementos)
        caracteristicasP1.update({caracteristica[0]: (signo, elemento)})
        
    elif caracteristica[0] == "---":
        flag = False
        
    # Se a caracteristica for qualquer outra
    else:
        caracteristicasP1.update({caracteristica[0]: (caracteristica[1])})
        
flag = True
while flag: # Caracteristicas da Pessoa 2
    try:
        caracteristica = input().split()
        
        if caracteristica[0] == "Musicas" or caracteristica[0] == "Filmes" or caracteristica[0] == "Series" or caracteristica[0] == "Livros":
            gostos = caracteristica
            caracteristica = gostos.pop(0)
            caracteristicasP2.update({caracteristica: gostos})
        
        elif caracteristica[0] == "Aniversario":
            signo, elemento = descobrirSigno(caracteristica[1], signos, elementos)
            caracteristicasP2.update({caracteristica[0]: (signo, elemento)})
            
        else:
            caracteristicasP2.update({caracteristica[0]: (caracteristica[1])})
            
    except EOFError:
        flag = False
    
# Resultados Finais
nomeShipado, pontos = shipador(nome1, nome2, pontos)
print(f"Hmmm, estou sentindo a conexão entre vocês... {nomeShipado} é um bom ship!")
print(f"Vocês combinam {calcularPontos(caracteristicasP1, caracteristicasP2, pontos)}%!")