mao = {}

for i in range(5):
    carta = input().split(" - ")
    mao[carta[0]] = int(carta[1])

for i in sorted(mao, key = mao.get):
    print(f"{i} - {mao[i]}")