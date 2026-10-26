def decodificar(frase, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nova_frase = ""

    for j in range(len(frase)):
        encontrou = False

        for i in range(len(alfabeto)):
            if frase[j] == alfabeto[i]:
                nova_frase += alfabeto[(i - chave) % len(alfabeto)]
                encontrou = True

        for i in range(len(alfabeto_maiusculo)):
            if frase[j] == alfabeto_maiusculo[i]:
                nova_frase += alfabeto_maiusculo[(i - chave) % len(alfabeto_maiusculo)]
                encontrou = True

        if not encontrou:
            nova_frase += frase[j]

    return nova_frase


def eNumeroPrimo(numero):
    if numero < 2:
        return False
    primo = True
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            primo = False
        i += 1
    return primo


def eQuadradoPerfeito(numero):
    if numero == 0:
        return False
    i = 0
    while i * i < numero:
        i += 1
    return i * i == numero


def temItem(inventarioH, nome, item):
    chaves = list(inventarioH[nome]["inventario"].keys())
    return item in chaves


def acharPorClasse(vivos, grupo, letra):
    resultado = ""
    for nome in vivos:
        if grupo[nome] == letra:
            resultado = nome
    return resultado


arma = ["cajado", "machado grande", "adaga", "adaga dupla"]
utilidade = ["grimorio", "escudo de madeira", "alaude", "ferramentas de ladrao"]
consumivel = ["pergaminho oculto", "racao de viagem", "pocao de cura", "bomba de fumaca"]
nomeClasse = {"B": "Bardo", "G": "Guerreiro", "L": "Ladino", "M": "Mago"}
classeIdeal = {
    "lira encantada": "B",
    "martelo do trovao": "G",
    "olho do abismo": "L",
    "orbe arcano": "M",
}
grupo = {}
vivos = []

print("Boa noite a todos!! Sejam bem vindos ao reino de Cinland. A aventura será longa, mas a gloria é eterna!!")
print("Vamos as apresentações.")

# PARTE 1 - PREPARAÇÃO
print()
inventarioH = {}
numero = 0
while numero < 1 or numero > 4:
    numero = int(input())
    if numero < 1 or numero > 4:
        print("Não tem toda essa gente pra jogar não.")

# laço dos herois
for i in range(numero):
    entrada = input().split(" ")
    nome = entrada[0]
    classe = entrada[1]
    inventarioH[nome] = {"inventario": {}}
    grupo.update({nome: classe})
    vivos.append(nome)

    # laço de criação dos inventário
    sequencia = ""
    while sequencia != "pronto":
        sequencia = input()
        if sequencia != "pronto":
            partes = sequencia.split(" - ")
            criptografada, chave, poderItem = partes[0], int(partes[1]), int(partes[2])
            descriptografada = decodificar(criptografada, chave)

            if descriptografada in arma:
                inventarioH[nome]["inventario"][descriptografada] = {"tipo": "arma", "poder": poderItem}
            elif descriptografada in utilidade:
                inventarioH[nome]["inventario"][descriptografada] = {"tipo": "utilidade", "poder": poderItem}
            elif descriptografada in consumivel:
                inventarioH[nome]["inventario"][descriptografada] = {"tipo": "consumivel", "poder": poderItem}

    # exibição do inventário do heroi
    inv = inventarioH[nome]["inventario"]
    if len(inv) == 0:
        print(f"{nome} ({nomeClasse[classe]}): sem itens")
    else:
        itens = []
        for item in inv.keys():
            itens.append(f"{item} [{inv[item]['tipo']}, {inv[item]['poder']}]")
        print(f"{nome} ({nomeClasse[classe]}): " + ", ".join(itens))

print("Grupo completamente apresentado, espero que todos estejam preparados para o que estar por vir.")

# PARTE 2 - DUNGEON
print()
print("Ao passa pelo arco de pedras, vocês encontram um lugar silencioso, com um odor nada agradável e um frio sem igual. Um calafrio na espinha os chama a recuar, mas a jornada começa aqui. Bem vindos a Dungeon do Grad5.")

linhas_colunas = int(input())
matriz = []

# criação da matriz
for i in range(linhas_colunas):
    linha = [int(x) for x in input().split(" ")]
    matriz.append(linha)

morreram = False
saiu = False
z, y = 0, 0

# movimentação na matriz
while not morreram and not saiu:
    casaAtual = matriz[z][y]

    # entrada
    if casaAtual == 0:
        print("Casa visitada: Entrada")

    # saída
    elif casaAtual == 99:
        print("Casa visitada: Saída")
        print("Vocês finalmente saem das cavernas escuras e frias. Mas não parece chegar em um lugar melhor.")
        saiu = True

    # número primo
    elif eNumeroPrimo(casaAtual):
        print("Casa visitada: Armadilha")
        tipo_armadilha = input()

        if tipo_armadilha == "flechas":
            guerreiro = acharPorClasse(vivos, grupo, "G")
            if guerreiro != "" and temItem(inventarioH, guerreiro, "escudo de madeira"):
                del inventarioH[guerreiro]["inventario"]["escudo de madeira"]
                print(f"O escudo de madeira de {guerreiro} protegeu o grupo.")
            else:
                morto = vivos.pop()
                print(f"{morto} sacrificou-se pelo grupo.")
                bardo = acharPorClasse(vivos, grupo, "B")
                if bardo != "" and temItem(inventarioH, bardo, "pocao de cura"):
                    del inventarioH[bardo]["inventario"]["pocao de cura"]
                    vivos.append(morto)
                    print(f"{bardo} usou a pocao de cura e salvou {morto}.")
                elif len(vivos) == 0:
                    morreram = True

        elif tipo_armadilha == "beholder":
            ladino = acharPorClasse(vivos, grupo, "L")
            if ladino != "" and temItem(inventarioH, ladino, "bomba de fumaca"):
                del inventarioH[ladino]["inventario"]["bomba de fumaca"]
                print(f"{ladino} usou a bomba de fumaça e o escaparam do Beholder.")
            else:
                print("Entraram em uma sala que não deveriam. A ultima visão é tudo ficando vermelho e em um flash, tudo fica preto. Vocês tão mortos.")
                morreram = True

    # quadrado perfeit
    elif eQuadradoPerfeito(casaAtual):
        print("Casa visitada: Looting")
        print("Finalmente um descanso! Aproveitam as maravilhas presentes na sala.")

        qtd_entradas = 1
        ladino = acharPorClasse(vivos, grupo, "L")
        if ladino != "" and temItem(inventarioH, ladino, "ferramentas de ladrao"):
            del inventarioH[ladino]["inventario"]["ferramentas de ladrao"]
            print(f"{ladino} arrombou o baú trancado!")
            qtd_entradas = 2

        # entradas
        for k in range(qtd_entradas):
            partes = input().split(" - ")
            item_especial = partes[0]
            cod_inventario = int(partes[1])

            # ordem lexicográfica
            letras = []
            for n in vivos:
                letras.append(grupo[n])
            letras.sort()
            letraDestino = letras[cod_inventario % len(letras)]
            destino = acharPorClasse(vivos, grupo, letraDestino)
            invDestino = inventarioH[destino]["inventario"]

            print(f"{item_especial} foi para {destino} ({nomeClasse[grupo[destino]]}).")

            # item foi para a classe ideal?
            if grupo[destino] == classeIdeal[item_especial]:
                for item in invDestino.keys():
                    invDestino[item]["poder"] = invDestino[item]["poder"] * 2
                print("O poder que esta em suas mãos é grandioso e parece chamar-lhe a glória eterna.")
            else:
                for item in invDestino.keys():
                    invDestino[item]["poder"] = invDestino[item]["poder"] * 125 // 100
                print("O poder é grande demais, você não consegue extrair o máximo dele.")

    # se nada, sala comum
    else:
        print("Casa visitada: Sala Comum")

    # para o maior vizinho
    if not morreram and not saiu:
        maiorVizinho = -1
        proxZ, proxY = z, y
        for dz, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nz, ny = z + dz, y + dy
            if 0 <= nz and nz < linhas_colunas and 0 <= ny and ny < linhas_colunas:
                if matriz[nz][ny] > maiorVizinho:
                    maiorVizinho = matriz[nz][ny]
                    proxZ, proxY = nz, ny
        z, y = proxZ, proxY

if morreram:
    print("Os sonhos e objetivos de todos são deixados no chão do Grad5. Nenhum de vocês restou. A glória nunca será alcançada!")

# PARTE 3
if not morreram:
    print()
    print("O lugar é silencioso. Até que, de repente, um rugido é ouvido. Uma criatura surge das sombras: o temido TarraByte!")

    entrada3 = input().split(" ")
    boss = {"hp": int(entrada3[0]), "ca": int(entrada3[1])}

    # iniciativas e ataques
    iniciativas = {}
    ataques = {}
    for nome in vivos:
        entrada4 = input().split(" ")
        iniciativas[nome] = int(entrada4[0])
        ataques[nome] = int(entrada4[1])

    # sorteando por ordem de iniciativa
    restantes = vivos.copy()
    ordem = []
    while len(restantes) > 0:
        melhor = restantes[0]
        for n in restantes:
            if iniciativas[n] > iniciativas[melhor]:
                melhor = n
        ordem.append(melhor)
        restantes.remove(melhor)

    print("Ordem de iniciativa: " + ", ".join(ordem))

    # ataques
    inspirado = False
    derrotado = False
    for nome in ordem:
        if not derrotado:
            inv = inventarioH[nome]["inventario"]
            classe = grupo[nome]
            rolagem = ataques[nome]

            # Bardo tem alaude?
            if classe == "B" and temItem(inventarioH, nome, "alaude"):
                print(f"{nome} inspirou o grupo.")
                inspirado = True
            else:
                bonus = 0
                if inspirado and (classe == "G" or classe == "L"):
                    bonus = 2

                dano = 0
                for item in inv.keys():
                    if inv[item]["tipo"] == "arma" and inv[item]["poder"] > dano:
                        dano = inv[item]["poder"]

                critico = False
                if rolagem == 20:
                    critico = True

                # ataque dos demais
                if critico or rolagem + bonus >= boss["ca"]:
                    if classe == "M" and temItem(inventarioH, nome, "pergaminho oculto"):
                        dano += inv["pergaminho oculto"]["poder"]
                        del inv["pergaminho oculto"]
                    elif classe == "G" and temItem(inventarioH, nome, "racao de viagem"):
                        dano += inv["racao de viagem"]["poder"]
                        del inv["racao de viagem"]

                    if critico:
                        dano = dano * 2
                        print(f"{nome} acertou um critico e causou {dano} de dano.")
                    else:
                        print(f"{nome} acertou e causou {dano} de dano.")

                    boss["hp"] -= dano
                    if boss["hp"] <= 0:
                        print(f"O TarraByte foi derrotado por {nome}!")
                        derrotado = True
                else:
                    print(f"{nome} errou o ataque.")

    if not derrotado:
        print(f"O TarraByte sobreviveu com {boss['hp']} de HP e obliterou o grupo. Fim da aventura.")