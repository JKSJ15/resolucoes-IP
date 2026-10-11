deuses = ["AFRODITE", "ARES", "ARTEMIS", "ATENA", "DEMETER", "DIONISIO", "HERMES", "POSEIDON", "ZEUS"]
msg_morte = "Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece tão bem."

print("O portão se abre diante de você, revelando o caminho para o Submundo. Uma nova tentativa começa agora.\n")

def calcular_legado(nome, titulo):
    legado_base  = 0
    if nome == "Hércules":
        legado_base = 50
    elif nome == "Aquiles":
        legado_base = 40
    elif nome == "Odisseu":
        legado_base = 35
    else:
        legado_base = 20

    if titulo == "Imortal":
        legado_base *= 1.5
    elif titulo == "Forte":
        legado_base *= 1.2
    elif titulo == "Grande":
        legado_base += 15
    else:
        legado_base += 10

    return legado_base

def obter_bencaos(bencaos):
    deus = ""
    numeroBencaos = 0
    while "PARAR" != deus:
        deus = input()
        if "PARAR" != deus:
            if deus in deuses:
                print(f"Zagreu obteve uma Bênção de {deus}.")
                bencaos.append(deus.upper())
                numeroBencaos += 1
            elif deus == "COMBINADA":
                combinada1 = input()
                combinada2 = input()
                if combinada1 not in deuses or combinada2 not in deuses:
                    print("Zagreu: Uma Bênção Combinada assim? Acho que você está brincando comigo.")
                elif combinada1 not in bencaos or combinada2 not in bencaos:
                    print("Zagreu: Eu ainda não tenho nenhuma Bênção desse(a) Deus(a), não posso combiná-la")
                else:
                    if combinada1 == combinada2:
                        print("Zagreu: Os dois Deuses precisam diferentes para realizar uma Bênção Combinada...")
                    elif combinada1 == "HERMES" or combinada2 == "HERMES":
                        print("Zagreu: Uma Bênção Combinada com Hermes? Acho que ele é competitivo demais pra cooperar com os outros.")
                    else:
                        print(f"Zagreu foi abençoado por uma Bênção Combinada de {combinada1} e {combinada2}.")
                        combinados = [combinada1, combinada2]
                        bencaos.append(combinados)
                        numeroBencaos += 1
                if combinada1 == "PARAR" or combinada2 == "PARAR":
                    print()
                    deus = "PARAR"
            else:
                print(f"Zagreu: Ah, claro. A Bênção de {deus}. Como pude esquecer? Tenho certeza de que meu pai também deve ter esquecido de mencioná-lo(a)... Você está brincando comigo não é?.")
        else:
            print()
    return bencaos

def tartaro(bencaos):
    linhaExilados = input()
    exilados = linhaExilados.split(", ")

    n = len(exilados)
    parar = False
    for i in range(n):
        if parar == False:
            trocou = False
            for j in range(0, n - i - 1):
                if exilados[j] > exilados[j + 1]:
                    exilados[j], exilados[j + 1] = exilados[j + 1], exilados[j]
                    trocou = True
            if not trocou:
                parar = True

    print("Zagreu: Aqui está sua papelada: " + ", ".join(exilados))
    print()

    numero_bencaos = 0
    bencaos = obter_bencaos(bencaos)
    if len(bencaos) < 3:
        return True, bencaos
    else:
        return False, bencaos

def asfodelo(bencaos):
    matriz1 = []
    linha = []
    for i in range(3):
        recebidos = input()
        linha = recebidos.split(" ")
        matriz1.append(linha)

    matriz2 = []
    for i in range(3):
        recebidos = input()
        linha = recebidos.split(" ")
        matriz2.append(linha)

    matriz_modificada = []
    r = [[0]*len(matriz2[0]) for _ in range(len(matriz1))]
    for a in range(len(matriz1)):
        for b in range(len(matriz2[0])):
            for c in range(len(matriz2)):
                r[a][b] += int(matriz1[a][c]) * int(matriz2[c][b])
    for row in r:
        matriz_modificada.append(row)

    maior = int(matriz_modificada[0][0])
    linha = 0
    coluna = 0
    for d in range(len(matriz_modificada)):
        for e in range(len(matriz_modificada)):
            if int(matriz_modificada[d][e]) > maior:
                maior = matriz_modificada[d][e]
                linha = d
                coluna = e

    print(f"Zagreu: devo lançar minha vara de pesca nesse ponto: ({linha}, {coluna})\n")

    bencaos = obter_bencaos(bencaos)
    if len(bencaos) < 6:
        return True, bencaos
    else:
        return False, bencaos

def elisio(bencaos):
    legado = 0
    while legado < 200:
        recebido = input()
        nome, titulo = recebido.split(" O ")
        legado_heroi = calcular_legado(nome, titulo)
        print(f"O Herói: {recebido} adicionou {legado_heroi} pontos de Legado.")
        legado += legado_heroi
        if legado >= 200:
            print("Zagreu: Acho que já fizemos história o suficiente por hoje.\n")

    bencaos = obter_bencaos(bencaos)
    if len(bencaos) < 9:
        return True, bencaos
    else:
        return False, bencaos

def templo_estigio():
    print("O Templo de Estige... o último obstáculo entre você e a superfície.\n")

    hpHades = 200
    hpZ = 100
    ataqueZ = 0
    ataqueH = 0
    danoH = 15
    danoH_especial = 50
    fase2 = False
    while hpZ > 0 and hpHades > 0:
        acaoZ = input()
        esquivou = False
        if acaoZ == "ATACAR":
            print("Zagreu golpeia Hades, causando 20 de dano.")
            hpHades -= 20
            ataqueZ += 1
        elif acaoZ == "ESQUIVA":
            print("Zagreu esquiva do ataque de Hades, evitando o dano.")
            esquivou = True
        else:
            print("Zagreu golpeia Hades com um ataque especial, causando 40 de dano.")
            hpHades -= 40
            ataqueZ += 1

        ataqueH += 1
        if esquivou == False and hpHades > 0:
            if hpHades <= 100 and fase2 == False:
                print()
                print("Hades: Chega! Isso acaba agora!\n")
                danoH = 25
                danoH_especial = 100
                fase2 = True
            if ataqueH %3 == 0:
                print("Hades: Desapareça!")
                print(f"Hades causou {danoH_especial} de dano em Zagreu.")
                hpZ -= danoH_especial
            else:
                print(f"Hades causou {danoH} de dano em Zagreu.")
                hpZ -= danoH
        if (ataqueH + 1) % 3 == 0 and hpZ > 0 and hpHades > 0:
            print("Zagreu: Meu pai parece estar carregando um forte ataque, é melhor desviar!")
    print()
    if hpHades <= 0:
        print("O senhor do Submundo cai diante de Zagreu. Pela primeira vez, não há nada entre ele e a superfície.")
        print("O portão se abre diante de você.")
        print("Zagreu finalmente deixa o Submundo para trás e sente o calor do sol tocar seu rosto. Pela primeira vez, a superfície está diante de seus olhos.")
        print("Você conseguiu escapar. A tentativa foi concluída.")
    else:
        print("Zagreu: Me desculpe, mãe. Foi tão perto...") 

bencaosR = []
passou, bencaosR = tartaro(bencaosR)
if passou:
    morte = True
    print(msg_morte)
else:
    passou, bencaosR = asfodelo(bencaosR)
    if passou:
        morte = True
        print(msg_morte)
    else:
        passou, bencaosR = elisio(bencaosR)
        if passou:
            morte = True
            print(msg_morte)
        else:
            templo_estigio()