isRaining = input().lower()
atualTemperature = int(input())
energy = int(input())
if isRaining == "s":
    if energy > 3:
        print("Brincar de bolinha no laboratório")
    else:
        print("Soneca na caminha do CIn")
else:
    if atualTemperature > 30:
        if energy > 3:
            print("Nadar no lago da UFPE")
        if energy <= 3:
            print("Descansar na sombra da árvore")
    
    elif atualTemperature <= 30 and atualTemperature >= 15:
        if energy > 2:
            print("Longo passeio no parque")
        if energy <= 2:
            print("Passeio curto no quarteirão")
    else:
        print("Passeio com roupinha de frio")