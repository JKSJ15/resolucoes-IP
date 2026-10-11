def verificar_mao(mao):
    copia = mao.copy()
    copia.insert(0, "x")
    marcados = []
    erros = 0

    for i in range(1, len(copia) // 2):
        if 2 * i < len(copia) and copia[i] < copia[2 * i]:
            marcados.append(2 * i)
            erros += 1
        if 2 * i + 1 < len(copia) and copia[i] < copia[2 * i + 1]:
            marcados.append(2 * i + 1)
            erros += 1

    filtrada = []
    for k in range(1, len(copia)):
        if k not in marcados:
            filtrada.append(copia[k])
    return filtrada, erros


def curingas_efetivos(curingas):
    efetivos = []
    for k in range(len(curingas)):
        if curingas[k] == "Blueprint":
            if k + 1 < len(curingas) and curingas[k + 1] != "Blueprint":
                efetivos.append(curingas[k + 1])
        else:
            efetivos.append(curingas[k])
    return efetivos


def calcular_base(erros):
    if erros == 0:
        return "Full House", 40, 4
    elif erros == 1:
        return "Três do mesmo", 30, 3
    elif erros == 2:
        return "Dois pares", 20, 2
    else:
        return "Carta Maior", 5, 1


def aplicar_curingas(efetivos, chips, mult):
    for c in efetivos:
        if c == "Joker":
            mult += 4
        elif c == "Space Joker":
            chips += 20
            mult += 1
    return chips, mult


def aplicar_arcanos(ativos, mao_filtrada, mult):
    nova = mao_filtrada.copy()

    if "Hierofante" in ativos:
        for i in range(len(nova)):
            if nova[i] < 30:
                nova[i] *= 2

    if "Justiça" in ativos:
        for x in nova:
            if x % 3 == 0:
                mult *= 1.1

    if "Força" in ativos:
        for i in range(len(nova)):
            if nova[i] >= 0 and int(nova[i] ** 0.5) ** 2 == nova[i]:
                nova[i] += 50

    return nova, mult


def calcular_pontuacao(chips_base, mao_filtrada, mult):
    chips_totais = chips_base + sum(mao_filtrada)
    pontuacao = int(chips_totais * round(mult, 2))
    return chips_totais, pontuacao


def jogar_rodada(mao, curingas, ativos):
    efetivos = curingas_efetivos(curingas)
    filtrada, erros = verificar_mao(mao)

    erros -= 2 * efetivos.count("Chicot")
    if erros < 0:
        erros = 0

    classificacao, chips, mult = calcular_base(erros)
    print(f"Classificação da mão: {classificacao}")

    chips, mult = aplicar_curingas(efetivos, chips, mult)
    filtrada, mult = aplicar_arcanos(ativos, filtrada, mult)
    chips_totais, pontuacao = calcular_pontuacao(chips, filtrada, mult)

    mult_exibido = round(mult, 2)
    if mult_exibido == int(mult_exibido):
        mult_exibido = int(mult_exibido)

    print(f"{chips_totais} chips x {mult_exibido} = {pontuacao}")
    return pontuacao


meta = eval(input())
print(f"Jimbo: Certo, você tem que conseguir {meta} chips. Boa sorte!")

inventario = eval(input())
curingas = []
arcanos = []

for j in inventario:
    if j in ["Joker", "Space Joker", "Blueprint", "Chicot"]:
        curingas.append(j)
    elif j in ["Tolo", "Hierofante", "Justiça", "Força"]:
        arcanos.append(j)

print("Curingas: " + ", ".join(curingas))
print("Arcanos: " + ", ".join(arcanos))

trocas = 4
jogadas = 0
total = 0
ativos = []

while jogadas < 4 and total < meta:
    mao = eval(input())
    acao = ""

    while acao != "Jogar":
        acao = input()

        if acao == "Jogar":
            jogadas += 1
            total += jogar_rodada(mao, curingas, ativos)
            ativos = []
            print(f"Total de chips: {total}")

        elif acao == "Trocar":
            if trocas > 0:
                nova_mao = eval(input())
                mao = nova_mao
                trocas -= 1

        elif acao == "Arcano":
            if len(arcanos) > 0:
                usado = arcanos.pop(0)
                if usado == "Tolo":
                    novo_arcano = input()
                    arcanos.append(novo_arcano)
                elif usado not in ativos:
                    ativos.append(usado)
                print("Arcanos: " + ", ".join(arcanos))

if total >= meta:
    print("Jimbo: Impressionante, você bateu a aposta.")
    if jogadas == 1:
        print("Jimbo: Balatro Balatrez esta a jugar balatro")
    elif jogadas == 4:
        print("Jimbo: Por pouco você falha, calculou bem.")
    else:
        print("Jimbo: Ainda bem que não apostei contra você.")
else:
    print(f"Jimbo: Mais que flop! Faltou {meta - total} chips.")