A = int(input())
L = int(input())
P = int(input())
H = int(input())

AL = (A + L + abs(A-L)) / 2
ALP = (AL + P + abs(AL-P)) / 2
M = ALP * H

print("%.0f" % M)

# x = (a + b + (|a - b|)) / 2 | abs()