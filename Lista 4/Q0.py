def qtd_inimigos(kills, vivos, rodada):
    return (10 * rodada + kills) - vivos

N = int(input())
rodada = 2
N -= 1

print("Haverá 10 inimigos na rodada 1")

for i in range(N):
    kills, vivos = input().split(" - ")
    
    print(f"Haverá {qtd_inimigos(int(kills), int(vivos), rodada)} inimigos na rodada {rodada}")

    rodada += 1