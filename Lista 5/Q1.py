def MDC(pokebolas, pocoes, revives):
    if pocoes == 0 and revives == 0:
        return pokebolas
    
    if not pocoes:
        if revives:
            return MDC(revives, pocoes, pokebolas % revives)
            
    else:
        return MDC(pocoes, pokebolas % pocoes, revives)
    
pokebolas = int(input())
pocoes = int(input())
revives = int(input())

result = MDC(pokebolas, pocoes, revives)

if result > 1:
    print(f"Gracas a Companhia Pokemon, {result} treinadores pokemon vao receber itens do Professor!")

else:
    print("Infelizmente apenas 1 treinador pokemon ira receber os itens hoje, e com certeza nao e o atrasado do Ash.")