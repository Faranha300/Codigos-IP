# Função para saber o poder da arma
def capicua(num):
    num_reverse = inverterNum(num)
    if num == num_reverse:
        return num
    num += num_reverse
    num_reverse = inverterNum(num)
    
    if num == num_reverse:
        return num
    else:
        return capicua(num)

# Função para inverter um numero
def inverterNum(num):
    num_reverse = str(num)
    num_reverse = num_reverse[::-1]
    num_reverse = int(num_reverse)
    return num_reverse

# Busca Binaria da arma dada uma lista
def busca(livros, inicio, fim, nome):
    if fim >= inicio:
        meio = (inicio + fim) // 2

        if nome in livros[meio]:
            return meio
        elif livros[meio] > nome:
            return busca(livros, inicio, meio-1, nome)
        elif livros[meio] < nome:
            return busca(livros, meio+1, fim, nome)

    else:
        return -1

N = int(input())
livros = []
chave = "Ghost Potrificationizer"

for i in range(N):
    livro = input()
    livros.append(livro)
    
posicao = busca(livros, 0, len(livros), chave)

if posicao != -1:
    num = (posicao+1) * 7
    poder = capicua(num)
    
    if poder < 50:
        print("É uma catástrofe, eu tenho a arma mas só posso usá-la uma vez")
        
    elif poder >= 50 and poder < 100:
        print("Terei que usar a minha arma com sabedoria!")
        
    elif poder >= 100 and poder < 200:
        print("A arma está bem carregada, me dei bem!")
    
    elif poder >= 200:
        print("Aha! EU NÃO TENHO MAIS MEDO DE NADA! PODEM VIR!")
        
else:
    print("Mamma mia! Só Mario poderá me salvar agora!")