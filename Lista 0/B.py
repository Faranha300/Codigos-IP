'''import math

X = int(input())
Z = int(input())

H = math.sqrt((X - 34)**2 + (Z - 220)**2)
K = math.sqrt((X)**2 + (Z)**2)
S = math.sqrt((X - 140)**2 + (Z - 456)**2)

print("Distancia para Hogsmeade: %.2f" % H)
print("Distancia para Kakariko: %.2f" % K)
print("Distancia para Solitude: %.2f" % S)'''

X = int(input())
Z = int(input())

H = ((X - 34)**2 + (Z - 220)**2)**0.5
K = (X**2 + Z**2)**0.5
S = ((X - 140)**2 + (Z - 456)**2)**0.5

print("Distancia para Hogsmeade: %.2f" % H)
print("Distancia para Kakariko: %.2f" % K)
print("Distancia para Solitude: %.2f" % S)