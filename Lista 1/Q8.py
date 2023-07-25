# Da pra comparar strings com os operadores <, >, <= e >=

N1 = str(input())
P1 = int(input())
N2 = str(input())
P2 = int(input())
N3 = str(input())
P3 = int(input())

if P1 > P2 and P1 > P3:
    if P2 > P3:
        print(N3, P3)
        print(N2, P2)
        print(N1, P1)
    
    elif P3 > P2:
        print(N2, P2)
        print(N3, P3)
        print(N1, P1)
        
    elif P2 == P3:
        if N2 > N3:
            print(N3, P3)
            print(N2, P2)
            print(N1, P1)
            
        elif N3 > N2:
            print(N2, P2)
            print(N3, P3)
            print(N1, P1)
    
elif P2 > P1 and P2 > P3:
    if P1 > P3:
        print(N3, P3)
        print(N1, P1)
        print(N2, P2)
    
    elif P3 > P1:
        print(N1, P1)
        print(N3, P3)
        print(N2, P2)
    
    elif P1 == P3:
        if N1 > N3:
            print(N3, P3)
            print(N1, P1)
            print(N2, P2)
        
        elif N3 > N1:
            print(N1, P1)
            print(N3, P3)
            print(N2, P2)
        
elif P3 > P1 and P3 > P2:
    if P1 > P2:
        print(N2, P2)
        print(N1, P1)
        print(N3, P3)
        
    elif P2 > P1:
        print(N1, P1)
        print(N2, P2)
        print(N3, P3)
        
    elif P1 == P2:
        if N1 > N2:
            print(N2, P2)
            print(N1, P1)
            print(N3, P3)
        
        elif N2 > N1:
            print(N1, P1)
            print(N2, P2)
            print(N3, P3)
    
elif P1 > P2 and P1 == P3 or P3 > P2 and P1 == P3:
    if N1 > N3:
        print(N2, P2)
        print(N3, P3)
        print(N1, P1)
    
    elif N3 > N1:
        print(N2, P2)
        print(N1, P1)
        print(N3, P3)
        
elif P1 > P3 and P1 == P2 or P2 > P3 and P1 == P2:
    if N1 > N2:
        print(N3, P3)
        print(N2, P2)
        print(N1, P1)
    
    elif N2 > N1:
        print(N3, P3)
        print(N1, P1)
        print(N2, P2)
        
elif P2 > P1 and P2 == P3 or P3 > P1 and P2 == P3:
    if N2 > N3:
        print(N1, P1)
        print(N3, P3)
        print(N2, P2)

    elif N3 > N2:
        print(N1, P1)
        print(N2, P2)
        print(N3, P3)

elif P1 == P2 and P2 == P3:
    if N1 > N2 and N1 > N3:
        if N2 > N3:
            print(N3, P3)
            print(N2, P2)
            print(N1, P1)
            
        elif N3 > N2:
            print(N2, P2)
            print(N3, P3)
            print(N1, P1)
    
    elif N2 > N1 and N2 > N3:
        if N1 > N3:
            print(N3, P3)
            print(N1, P1)
            print(N2, P2)
        
        elif N3 > N1:
            print(N1, P1)
            print(N3, P3)
            print(N2, P2)
            
    elif N3 > N1 and N3 > N2:
        if N1 > N2:
            print(N2, P2)
            print(N1, P1)
            print(N3, P3)
        
        elif N2 > N1:
            print(N1, P1)
            print(N2, P2)
            print(N3, P3)