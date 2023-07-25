# Função para descobrir se um dado candidato é um espião, ela retorna um operador lógico e a porcentagem do candidato ser espião
def descobrirEspiao(nome ,idade, empresa_antiga, anos_trabalhados, rivais):
    if nome in pessoas:
        print(f"{nome} ja esta participando da avaliacao!")
        return False, 0
    
    else:
        if empresa_antiga in rivais:
            porcentagem = anos_trabalhados / idade
            
            if idade >= 50 and porcentagem >= 0.30:
                if empresa_antiga == rivais[0]:
                    porcentagem += porcentagem * 0.15
                elif empresa_antiga == rivais[1]:
                    porcentagem += porcentagem * 0.10
                elif empresa_antiga == rivais[2]:
                    porcentagem += porcentagem * 0.05
                
            elif idade <= 30 and porcentagem >= 0.40:
                if empresa_antiga == rivais[0]:
                    porcentagem += porcentagem * 0.30
                elif empresa_antiga == rivais[1]:
                    porcentagem += porcentagem * 0.25
                elif empresa_antiga == rivais[2]:
                    porcentagem += porcentagem * 0.20
                
            elif porcentagem > 0.20:
                if empresa_antiga == rivais[0]:
                    porcentagem += porcentagem * 0.10
                elif empresa_antiga == rivais[1]:
                    porcentagem += porcentagem * 0.05
                elif empresa_antiga == rivais[2]:
                    porcentagem += porcentagem * 0.03
                    
            porcentagem *= 100
            return True, int(porcentagem)
        
        else:
            print(f"Nao ha ligacoes entre {nome} e as empresas concorrentes, prossiga tranquilamente com a entrevista.")
            return False, 0

pessoas = {}
empresasRivais = []
espioes = []
flag = True

for i in range(3): # Empresas Rivais
    empresa = input()
    empresasRivais.append(empresa)

while flag:
    try: # Try except para parar o loop no dikastis
        nome, idade, empresa_antiga, anos_trabalhados = input().split()
        
        espiao, porcentagem = descobrirEspiao(nome ,int(idade), empresa_antiga, int(anos_trabalhados), empresasRivais)
        if espiao:
            espioes.append(nome)
            pessoas.update({nome: (int(idade), empresa_antiga, int(anos_trabalhados), porcentagem)})
        
    except EOFError:
        flag = False

# Saída com os dados dos espiões
print("[ALERTA]! A SEGUIR UMA LISTA DOS POSSIVEIS ESPIOES")
for i in espioes:
    print(f"{i}:")
    print(f"- Idade: {pessoas.get(i)[0]}")
    print(f"- Antiga corporacao: {pessoas.get(i)[1]}")
    print(f"- Anos trabalhos: {pessoas.get(i)[2]}")
    print(f"- Probabilidade de ser espiao: {pessoas.get(i)[3]}%")