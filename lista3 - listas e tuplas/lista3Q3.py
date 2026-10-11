nome_do_vendedor = ""
nome_da_empresa = ""
parar = False

vendedores = ["Dwight","Jim","Stanley","Phillips"]

Dwight = []
Jim = []
Stanley = []
Phillips = []
Michael = []

while parar == False:
    nome_do_vendedor = input()
    if "fim" in nome_do_vendedor.lower():
        parar = True
    else:
        nome_da_empresa = input()
        if nome_do_vendedor in vendedores:
            if "Dwight" in nome_do_vendedor:
                Dwight.append(nome_da_empresa)
            elif "Jim" in nome_do_vendedor:
                Jim.append(nome_da_empresa)
            elif "Stanley" in nome_do_vendedor:
                Stanley.append(nome_da_empresa)
            elif "Phillips" in nome_do_vendedor:
                Phillips.append(nome_da_empresa)
        else:
            Michael.append(nome_da_empresa)

if len(Dwight) >= 1:
    print(f"Dwight : {Dwight}")
else:
    print("Dwight fez zero vendas hoje. Mais sorte amanhã!")
if len(Jim) >= 1:
    print(f"Jim : {Jim}")
else:
    print("Jim passou o dia fazendo pegadinhas e não concluiu nenhuma venda!")
if len(Stanley) >= 1:
    print(f"Stanley : {Stanley}")
else:
    print("Stanley acabou dormindo em serviço, amanhã ele estará mais descansado!")
if len(Phillips) >= 1:
    print(f"Phillips : {Phillips}")
else:
    print("Phillips se distraiu e acabou não fazendo vendas hoje!")
if len(Michael) >= 1:
    print("Michael realizou vendas hoje!")
    print(f"Michael : {Michael}")
else:
    print("Michael não trabalhou como vendedor hoje, apenas foi um bom chefe.")