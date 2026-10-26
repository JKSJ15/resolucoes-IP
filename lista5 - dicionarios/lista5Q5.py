INVENTARIO = {
    "nível": 0,
    'magias': [],
    'itens': {
        "pás": ["Pá do herói"],
    },
    'troféus': {
        'Capacete do Espectro': 0,
        'Capacete Gélido': 0
    }
}
ITENS = {
    "F": {"secao": "magias", "nome": "Varinha de Chamas", "mensagem": "O que é isso? Sinto um fogo emanando do fundo da minha alma…"},
    "V": {"secao": "magias", "nome": "Varinha de Gelo", "mensagem": "Uma magia nova é sempre bom!"},
    "P": {"secao": "pás", "nome": "Pá Espectral", "mensagem": "Uma pá transparente, que loucura!"},
    "p": {"secao": "pás", "nome": "Pá comum", "mensagem": "Mais uma para minha coleção."},
}
CHEFES = {
    "Specter Knight": {"capacete": "Capacete do Espectro", "nivel_minimo": 2},
    "Polar Knight": {"capacete": "Capacete Gélido", "nivel_minimo": 5},
}
DIRECOES = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}


# enfrentar chefes
def enfrentar(chefe, inventario, nivel, tem_requisito):
    capacete = CHEFES[chefe]["capacete"]
    nivel_minimo = CHEFES[chefe]["nivel_minimo"]
    if nivel >= nivel_minimo and tem_requisito:
        inventario["troféus"][capacete] = 1
        return True
    else:
        return False


# coletar itens
def coletar(letra, inventario):
    secao = ITENS[letra]["secao"]
    nome = ITENS[letra]["nome"]
    mensagem = ITENS[letra]["mensagem"]
    print(mensagem)
    if secao == "pás":
        inventario["itens"]["pás"].append(nome)
    else:
        inventario["magias"].append(nome)


# movimentar no mapa
def movimentar(mapa, inventario, chefe):
    chegouX = False
    posicao = (0, 0)
    while not chegouX:
        simbolo = input()
        movimento = DIRECOES.get(simbolo, (0, 0))

        # valida proximo movimento para evitar fugas
        proxL = posicao[0] + movimento[0]
        proxC = posicao[1] + movimento[1]
        if 0 <= proxL <= 4 and 0 <= proxC <= 4:
            posicao = (proxL, proxC)

            # verifica as letras
            if posicao in mapa:
                letra = mapa[posicao]

                if letra in ITENS:
                    coletar(letra, INVENTARIO)
                    mapa.pop(posicao)

                elif letra == "N":
                    inventario["nível"] += 1
                    mapa.pop(posicao)

                elif letra == "X":
                    if chefe == "Specter Knight":
                        print("Está na hora de caçar fantasmas!")
                    else:
                        print("Polar Knight! O que você está fazendo aqui?")
                        print("Como pode trair nosso juramento?")
                    chegouX = True

    return chegouX

def derrota():
    print("A jornada do herói chega a um triste fim…")
    print("Sua pá não foi capaz de cavar uma saída desse buraco de trevas em que estamos.")
    print("O que restou? Nada… brutal.")
    print()

print("Shovel Knight, o lendário guerreiro, está de volta! Salvai-nos, ó herói da pá!")
print()

# MERCADOR
magias_catalogo = ["Pergaminho dos Elementos", "Varinha da Água", "Grimório de 4 folhas"]
pergaminho = False
varinha = False
grimorio = False
pegar = input()

if pegar == "sim":
    escolha = input()

    if escolha == "Pergaminho dos Elementos":
        pergaminho = True
    elif escolha == "Varinha da Água":
        varinha = True
    elif escolha == "Grimório de 4 folhas":
        grimorio = True

    if escolha in magias_catalogo:
        INVENTARIO["magias"].append(escolha)

# CEMITÉRIO - Specter Knight
print("======== CEMITÉRIO DOS LICHS ========")
print("Um antigo vilarejo tomado pelos mortos. Me pergunto se aquele cavaleiro fantasma se esconde por aqui…")
print("Black Knight? O que fazes aqui?")

# desafio
if pergaminho or varinha or grimorio:
    print("Isso era um desafio?")
    print()

    # exploração
    mapa_cemiterio = {
        (0, 2): "p",
        (1, 4): "P",
        (2, 1): "N",
        (2, 2): "N",
        (2, 3): "F",
        (3, 3): "N",
        (3, 4): "N",
        (4, 0): "p",
        (4, 1): "X",
    }
    movimentar(mapa_cemiterio, INVENTARIO, "Specter Knight")
    requisito_cumprido = "Pá Espectral" in INVENTARIO["itens"]["pás"]
    venceu = enfrentar("Specter Knight", INVENTARIO, INVENTARIO["nível"], requisito_cumprido)

    # NAVIO - Polar Knight
    if venceu:
        print()
        print("======== NAVIO ENCALHADO ========")
        print("Uma embarcação antiga do Rei liderada pelo meu antigo mentor, o que será que encontrarei?")
        print("Você de novo? E que neve toda é essa?")

        # desafio
        passou = False
        if len(INVENTARIO["itens"]["pás"]) >= 3:
            print("Engraçado tentar parar um mestre das pás com neve, você se superou dessa vez!")
            passou = True
        else:
            if (INVENTARIO["nível"] - 3) > 0:
                print("Que saco! Onde estão minhas outras pás?")
                INVENTARIO["nível"] -= 3
                passou = True

        if passou:
            print()
            # exploração
            mapa_navio = {
                (0, 4): "X",
                (1, 3): "N",
                (2, 1): "N",
                (2, 2): "N",
                (3, 3): "N",
                (4, 1): "V",
            }
            movimentar(mapa_navio, INVENTARIO, "Polar Knight")
            tem_requisito = len(INVENTARIO["magias"]) >= 2
            venceu3 = enfrentar("Polar Knight", INVENTARIO, INVENTARIO["nível"], tem_requisito)

            # TORRE - FINAL
            if venceu3:
                print()
                print("======== TORRE DO DESTINO ========")
                print("Finalmente, aqui de novo…")

                pas = INVENTARIO["itens"]["pás"]
                print(f"ANTES - pás: {pas}")

                INVENTARIO["itens"]["pás"] = ["coragem do cavaleiro"]
                print(f"DEPOIS - pás: {INVENTARIO['itens']['pás']}")

                print("Perdi minhas pás, mas não posso recuar, agora é tudo ou nada!")

                acao = ""
                while acao != "Droga, não tenho mais nada de mana!":
                    acao = input()
                    lista = acao.split()
                    if "morte" in lista:
                        INVENTARIO["nível"] -= 2
                        print("Não posso recuar de jeito nenhum! Irei superar meus limites aqui e agora!")
                    elif "magia" in lista or "feitiço" in lista:
                        INVENTARIO["nível"] -= 1
                        print("Não posso recuar de jeito nenhum! Irei superar meus limites aqui e agora!")

                if INVENTARIO["nível"] > 0:
                    print("Minha amada! Finalmente pude revê-la e livrá-la desta terrível maldição!")
                    print("Vamos embora deste lugar amaldiçoado!")
                    print()
                else:
                    derrota()
            else:
                derrota()
        else:
            derrota()
    else:
        derrota()
else:
    derrota()

# relatório final
print("======== RELATÓRIO FINAL ========")
magias = INVENTARIO["magias"]
pasF = INVENTARIO["itens"]["pás"]
capacetes = []
for nome_capacete, valor in INVENTARIO["troféus"].items():
    if valor > 0:
        capacetes.append(nome_capacete)

if len(capacetes) > 0:
    print("CAPACETES: " + ", ".join(capacetes))
else:
    print("CAPACETES: NENHUM")

if len(magias) > 0:
    print("MAGIAS: " + ", ".join(magias))
else:
    print("MAGIAS: NENHUM")

print("PÁS: " + ", ".join(pasF))