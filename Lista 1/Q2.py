Nome = str(input())
valor_semestre1 = int(input())
valor_semestre2 = int(input())

media = int((valor_semestre1 + valor_semestre2) / 12)

if ((Nome == "Jim Halpert") or (Nome == "Dwight Schrute") or (Nome == "Phyllis Vance") or (Nome == "Stanley Hudson")):
    if media <= 50:
        print(f"{Nome}, voce so vendeu {media:.0f} por mes? Voce ta demitido... Brincadeira!")

    elif media < 100:
        print(f"{Nome}, voce mandou mal... Vai ter que pagar meu almoco.")
    
    elif media >= 100:
        print(f"Parabens, {Nome}! Voce foi promovido! kkkkk Brincadeira, a matriz que decide!")

else:
    print("Sinto muito, mas so os vendedores eh que vao ganhar a viagem pra matriz.")