def slots_sobrando(slots_totais, slots_ocupados):
    return slots_totais - slots_ocupados

def slots_pochetes(slots_totais, qtd_pochetes):
    return slots_totais + (qtd_pochetes * 2)

slots_totais = int(input())
slots_ocupados = int(input())
inventario = []

for i in range(slots_ocupados):
    item = input().split(" - ")
    
    inventario.append(item)

qtd_pochetes = int(input())

print(f"Voce possui {slots_totais} slots no inventario e {slots_ocupados} estao ocupados.")
print(f"Espacos sobrando [{slots_sobrando(slots_totais, slots_ocupados)}]\n")

if len(inventario) > 0:
    print("Lista de itens:")
    for i in range(len(inventario)):
        print(f"{inventario[i][0]} [{inventario[i][1]}]")
else:
    print("Seu inventário ainda está vazio. Que sorte... ou azar. Tome cuidado.")
    
if qtd_pochetes > 0:
    print(f"\nVoce conseguiu {qtd_pochetes} pochete(s) e agora possui {slots_pochetes(slots_totais, qtd_pochetes)} slots de inventario.")
    print(f"Espacos sobrando [{slots_pochetes(slots_totais, qtd_pochetes) - slots_ocupados}]")
else:
    print("\nVocê ainda não encontrou pochetes. Seus espaços continuam os mesmos.")