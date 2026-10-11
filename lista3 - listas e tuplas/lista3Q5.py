Força = ""
Resistência= ""
Velocidade= ""
Inteligência= ""
Experiência= ""

heroi = ""
herois = []
partes = []
partesAm = []
ameacas = []

print("========================================")
print("GDA - HERO DISPATCH SYSTEM")
print("========================================")
print("[ROBOT] Sistema de despacho iniciado.")

parar = False
while parar == False:
    heroi = input()
    if "FIM" in heroi.upper():
        parar = True
    else:
        herois.append(heroi)

print(f"[ROBOT] {len(herois)} heróis disponíveis.")

num = int(input())
i = 0
for i in range(num):
    ameaca = input()
    partesAm = ameaca.split(" - ")
    NomeAm = partesAm[0]
    ForçaAm = int(partesAm[1])
    AtributoPrioritario = partesAm[2]
    ameacas.append(ameaca)

    print("========================================")
    print("NOVA AMEAÇA DETECTADA")
    print("========================================")
    print(f"AMEAÇA: {NomeAm}")
    print(f"NÍVEL DE DIFICULDADE: {ForçaAm}")
    print(f"PRIORIDADE: {AtributoPrioritario}")
    print("[ROBOT] Analisando heróis disponíveis...")
    print("[ROBOT] Calculando compatibilidade...")
    print("[ROBOT] Análise concluída.")

    ranking = []
    for k in range(len(herois)):
        partes = herois[k].split(" - ")
        forca = int(partes[1])
        resistencia = int(partes[2])
        velocidade = int(partes[3])
        inteligencia = int(partes[4])
        experiencia = int(partes[5])

        pontuacao = forca + resistencia + velocidade + inteligencia + experiencia

        if "força" in AtributoPrioritario.lower():
            pontuacao += forca
            valorPrioritario = forca
        elif "resistência" in AtributoPrioritario.lower():
            pontuacao += resistencia
            valorPrioritario = resistencia
        elif "velocidade" in AtributoPrioritario.lower():
            pontuacao += velocidade
            valorPrioritario = velocidade
        elif "inteligência" in AtributoPrioritario.lower():
            pontuacao += inteligencia
            valorPrioritario = inteligencia
        elif "experiência" in AtributoPrioritario.lower():
            pontuacao += experiencia
            valorPrioritario = experiencia

        ranking.append([partes[0], pontuacao, valorPrioritario])

    tamanho = len(ranking)
    for a in range(tamanho):
        for b in range(tamanho - 1 - a):
            atual = ranking[b]
            proximo = ranking[b+1]
            trocar = False
            if proximo[1] > atual[1]:
                trocar = True
            elif proximo[1] == atual[1] and proximo[2] > atual[2]:
                trocar = True
            if trocar:
                ranking[b] = proximo
                ranking[b+1] = atual

    print("========================================")
    print("RANKING DE HERÓIS")
    print("========================================")
    posicao = 1
    for r in ranking:
        print(f"{posicao}. {r[0]} - {r[1]} pontos")
        posicao += 1
    print("----------------------------------------")

    if ForçaAm <= 30:
        classificacao = "SIMPLES"
        qtd_necessaria = 1
    elif ForçaAm <= 70:
        classificacao = "MODERADA"
        qtd_necessaria = 2
    else:
        classificacao = "CRÍTICA"
        qtd_necessaria = 3

    print(f"[ROBOT] Ameaça {classificacao}.")
    print(f"[ROBOT] {qtd_necessaria} herói(s) serão despachados.")

    qtd_disponivel = len(herois)
    if qtd_disponivel < qtd_necessaria:
        print("[ROBOT] ALERTA!")
        print(f"[ROBOT] São necessários {qtd_necessaria} heróis,")
        print(f"[ROBOT] mas apenas {qtd_disponivel} estão disponíveis.")
        print("[ROBOT] Despachando todos os heróis disponíveis.")
        qtd_enviar = qtd_disponivel
    else:
        print("[CECIL] Equipe selecionada para a missão.")
        qtd_enviar = qtd_necessaria

    print("EQUIPE DESPACHADA:")
    for k in range(qtd_enviar):
        print(f"> {ranking[k][0]}")
    print("========================================")