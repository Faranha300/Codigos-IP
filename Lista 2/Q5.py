letra = str(input()).upper()
i = 0

if letra == "X" or letra == "T" or letra == "O":
    numero = int(input())
    impar = numero % 2
        
    if numero > 1 and impar == 1:
        if letra == "T":
            while i < numero:
                if i == 0:
                    print("X" * numero + "\n")
                
                elif i == numero - 1:
                    print("0" * int(numero/2) + "X" + "0" * int(numero/2))
            
                elif i > 0 and not i == numero - 1:
                    print("0" * int(numero/2) + "X" + "0" * int(numero/2) + "\n")
            
                i += 1

        elif letra == "O":
            while i < numero:
                if i == 0:
                    print("X" * numero + "\n")
                    
                elif i == numero - 1:
                    print("X" * numero)
                    
                elif i > 0 and not i == numero - 1:
                    print("X" + "0" * (numero - 2) + "X\n")
                
                i += 1
        
        elif letra == "X":
            while i < numero:
                if i == 0:
                    print("X" + "0" * (numero - 2) + "X\n")
                    i += 1
                
                elif i > 0 and i < int(numero / 2) and not i == int(numero / 2):
                    n = numero - 4
                    while n > 0:
                        print("0" * (i) + "X" + "0" * (n) + "X" + "0" * (i) + "\n")
                        i += 1
                        n -= 2
                        
                elif i == int(numero / 2):
                    print("0" * int(numero / 2) + "X" + "0" * int(numero / 2) + "\n")
                    i += 1
                
                elif i > 0 and i > int(numero / 2) and not i == int(numero / 2) and not i == numero - 1:
                    n = 0
                    x = int(numero / 2)
                    while i < numero - 1:
                        print("0" * (x - 1) + "X" + "0" * (n + 1) + "X" + "0" * (x - 1) + "\n")
                        x -= 1
                        i += 1
                        n += 2
                
                elif i == numero - 1:
                    print("X" + "0" * (numero - 2) + "X")
                    i += 1
                    
    else:
        print("Entrada não permitida")
                    
else:
    print("Entrada não permitida")