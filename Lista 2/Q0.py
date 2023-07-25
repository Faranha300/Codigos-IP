n_competidores = int(input())
quant_V = 0

while n_competidores > 0:
    competidor = input()
    quant_lat = int(input())
    
    if quant_lat > quant_V:
        quant_V = quant_lat
        competidor_V = competidor
        
    n_competidores -= 1
    
else:
    print(f"{competidor_V} e o novo anjo!")