N_festas = int(input())
cervejaf = 0
vodcaf = 0
caipirinhaf = 0

while N_festas > 0:
    N_copos = int(input())
    cerveja = 0
    vodca = 0
    caipirinha = 0 
    
    while N_copos > 0:
        bebida = str(input())
        
        if bebida == "cerveja":
            cerveja += 1
            cervejaf += 1
            
        elif bebida == "vodca":
            vodca += 1
            vodcaf += 1
            
        elif bebida == "caipirinha":
            caipirinha += 1
            caipirinhaf += 1
        
        N_copos -= 1
        
    if cerveja > vodca and cerveja > caipirinha:
        print(f"O que ele mais tomou nessa festa foi: cerveja")
            
    elif vodca > cerveja and vodca > caipirinha:
        print(f"O que ele mais tomou nessa festa foi: vodca")
        
    elif caipirinha > cerveja and caipirinha > vodca:
        print(f"O que ele mais tomou nessa festa foi: caipirinha")

    N_festas -= 1
    
else:
    print(f"cerveja - {cervejaf}")
    print(f"caipirinha - {caipirinhaf}")
    print(f"vodca - {vodcaf}")