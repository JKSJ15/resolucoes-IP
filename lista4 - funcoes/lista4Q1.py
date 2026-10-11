def selecionar_personagem(personagemSel):
    personagem = personagemSel
    if "Cavaleiro" in personagem:
        hpPersonagem = 55
        limite = 55
    elif "Paladino" in personagem:
        hpPersonagem = 80
        limite = 80
    elif "Sacerdotisa" in personagem:
        hpPersonagem = 60
        limite = 60
    elif "Necromante" in personagem:
        hpPersonagem = 40
        limite = 40
    elif "Assassino" in personagem:
        hpPersonagem = 45
        limite = 45
    elif "Bruxa" in personagem:
        hpPersonagem = 50
        limite = 50

    print(f"O(A) {personagem} é o(a) herói(na) lendário(a) escolhido(a)!")
    return hpPersonagem, limite, personagem

def aplicar_efeito_sala(sinal, hp, personagem):
    if sinal == "+":
        hp += 20
    elif sinal == "c":
        hp -= 15
        if hp > 0:
            print(f"O(A) {personagem} prevalece no combate, mantendo-se firme com {hp} HP!")
    elif sinal == "@":
        hp -= 25
    return hp

def movimentar(matriz, comandos, hp, limite, personagem):
    x, y = 0, 0
    passos = 0
    passou = False

    for comando in comandos:
        novo_x, novo_y = x, y

        if comando == ">":
            novo_y += 1
        elif comando == "<":
            novo_y -= 1
        elif comando == "v":
            novo_x += 1
        elif comando == "^":
            novo_x -= 1

        if 0 <= novo_x < 5 and 0 <= novo_y < 5:
            x, y = novo_x, novo_y
            passos += 1

            hp = aplicar_efeito_sala(matriz[x][y], hp, personagem)

            if hp > limite:
                hp = limite

            if hp <= 0:
                return hp, passos, passou

            if matriz[x][y] == "@":
                if hp > 0:
                    passou = True
                    return hp, passos, passou
                else:
                    return hp, passos, passou

    return hp, passos, passou

print("A jornada pela Pedra Mágica tem início! O destino do reino está selado, e esta guerra finalmente encontrará o seu fim.\n")

personagem = input()
hpPersonagem, limite, personagem = selecionar_personagem(personagem)

matriz = []
for i in range(5):
    valores = input().split()
    matriz.append(valores)

movimentos = input()
comandos = list(movimentos)

hpPersonagem, passos, resultado = movimentar(matriz, comandos, hpPersonagem, limite, personagem)

if resultado is True:
    print("A profecia se cumpriu e a paz reina mais uma vez!")
    print(f"Cruzando as profundezas da masmorra em {passos} passos de pura bravura, o(a) nosso(a) herói(na) ergue-se triunfante com {hpPersonagem} HP.")
elif resultado is False:
    print("Ainda não é o fim! A jornada continua…\n")

    personagem = input()
    hpPersonagem, limite, personagem = selecionar_personagem(personagem)

    matriz_transposta = []
    for i in range(len(matriz[0])):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        matriz_transposta.append(linha)
    matriz = matriz_transposta

    movimentos = input()
    comandos = list(movimentos)

    hpPersonagem, passos, resultado = movimentar(matriz, comandos, hpPersonagem, limite, personagem)

    if resultado is True:
        print("A profecia se cumpriu e a paz reina mais uma vez!")
        print(f"Cruzando as profundezas da masmorra em {passos} passos de pura bravura, o(a) nosso(a) herói(na) ergue-se triunfante com {hpPersonagem} HP.")
    else:
        print("Sem heróis. Sem esperança. O Reino caiu.")
