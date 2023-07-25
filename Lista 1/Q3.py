CoordA = int(input())
CoordB = int(input())
r = int(input())
CoordX = int(input())
CoordY = int(input())

if r > 0:
    distancia = ((CoordA - CoordX)**2 + (CoordB - CoordY)**2)**0.5
    
    if distancia < r + 2:
        print("Esferas do dragao detectadas")  
         
    else:
        print("Esferas fora do radar")

else:
    print("Sua amplitude esta baixa, nao conseguimos te localizar no radar")