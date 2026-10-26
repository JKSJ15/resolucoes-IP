inventario = {}
acao = ""

# looping
while acao != "FIM":
    acao = input()

    # adicionar
    if acao == "ADICIONAR":
        item = input()
        quant = int(input())

        if item in inventario:
            quantAtual = inventario[item]
            inventario[item] = quant + quantAtual
        else:
            inventario[item] = quant

    # remover
    elif acao == "REMOVER":
        item = input()
        quant = int(input())

        if item in inventario:
            quantAtual = inventario[item]

            if quantAtual < quant:
                print("ERRO! Quantidade insuficiente no Inventário!")
            else:
                inventario[item] = quantAtual - quant
                if inventario[item] <= 0:
                    del inventario[item]
        else:
            print("ERRO! Item não está no Inventário!")

# verificação do tamanho do inventário
if len(inventario) != 0:
    chaves = list(inventario.keys())
    valores = list(inventario.values())

    # exibição do inventário
    for i in range(len(inventario)):
        print(chaves[i],"-",valores[i])
else:
    print("Inventário Vazio!")
    