cartas_raras = ["urayuli", "louva-a-deus rei", "ameba", "tubarão", "urso"]
canideos = ["lobo", "coiote", "cachorro"]
insetos = ["louva-a-deus", "abelha", "formiga"]
aves = ["corvo", "urubu", "pardal"]
cervideos = ["antilocapra", "alce", "caribu"]
repteis = ["rã", "tartaruga", "víbora"]

def carta_tem_classe(carta, classe):
    classe = classe.lower()
    carta_lower = carta.lower()
    if classe == "canideos":
        for animal in canideos:
            if animal in carta_lower:
                return True
    elif classe == "insetos":
        for animal in insetos:
            if animal in carta_lower:
                return True
    elif classe == "aves":
        for animal in aves:
            if animal in carta_lower:
                return True
    elif classe == "cervideos":
        for animal in cervideos:
            if animal in carta_lower:
                return True
    elif classe == "repteis":
        for animal in repteis:
            if animal in carta_lower:
                return True
    return False

def batalha(chefe, coeficienteJ, baralho, totem):
    venceu = False
    if chefe == "Garimpeiro":
        cChefe = 40
        if coeficienteJ == 0:
            coeficienteJ = 0
        else:
            coeficienteJ = coeficienteJ//2
        if cChefe < coeficienteJ:
            print("Garimpeiro - Oxe!")
            venceu = True
        elif cChefe == coeficienteJ:
            print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
        else:
            print("Garimpeiro - Mais ouro pra mim!")
        return venceu
    
    elif chefe == "Pescador":
        if len(baralho) == 0:
            cChefe = 90
        else:
            cChefe =90 + (coeficienteJ // len(baralho))

        if cChefe < coeficienteJ:
            venceu = True
            print("Pescador - Vai pescar...")
        elif cChefe == coeficienteJ:
            print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
        else:
            print("Pescador - Hum. Vai pescar.")
        return venceu

    elif chefe == "Comerciante":
        cChefe = 160
        for carta, coef in baralho:
            if "pele" in carta.lower():
                cChefe -= 10
                coeficienteJ += 10

        if cChefe < coeficienteJ:
            print("Comerciante - Hmm... muito bem.")
            venceu = True
        elif cChefe == coeficienteJ:
            print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
        else:
            print("Comerciante - Você vai virar uma pele deslumbrante.")
        return venceu
    
def montar_baralho(cartas):
    baralho = []
    for carta in cartas:
        if "pele" in carta.lower():
            baralho.append((carta, 0))
        elif "filhote de" in carta.lower() or "ovo de" in carta.lower():
            baralho.append((carta, 5))
        elif tem_rara(carta):
            baralho.append((carta, 20))
        else:
            baralho.append((carta, 10))
    return baralho

def tem_rara(carta):
    carta_lower = carta.lower()
    for rara in cartas_raras:
        if rara in carta_lower:
            return True
    return False

def receberItens(totem=""):
    item = ""
    itens = []
    while item != "FIM":
        item = input()
        if item != "FIM":
            if item.lower() == "totem":
                classe_totem = input()
                totem = classe_totem.lower()
                print(f"Totem ativo: {classe_totem.capitalize()}")
            else:
                if  len(itens) < 3:
                    itens.append(item)
                else:
                    print("Inventario cheio")
    return itens, totem

def calcular_coeficienteJogador(baralho, totem, itens):
    total = 0
    for carta, coeficiente in baralho:
        if carta_tem_classe(carta, totem.lower()):
            total += coeficiente * 2
        else:
            total += coeficiente

    for item in itens:
        sem_espacos = item.replace(" ", "")
        total += len(sem_espacos)
    return total

def receber_cartas():
    cartas = []
    carta = ""
    while "FIM" != carta.upper():
        carta = input()
        if "FIM" != carta.upper():
            cartas.append(carta)
    return cartas

print("Leshy - Outro desafiante. Já faz tanto tempo...")

#FASE 1
print("Leshy - O sol banha os abetos sonolentos, você adentrou o... matagal.")
carta = ""
cartas = receber_cartas()
baralho = montar_baralho(cartas)
print(f"{len(cartas)} cartas foram adicionadas ao baralho")

itens, totem = receberItens()
print("Itens no inventario: " + ", ".join(itens))
cJogador = calcular_coeficienteJogador(baralho, totem, itens)

print("Garimpeiro - É o Garimpeiro! OPA!")
venceu = batalha("Garimpeiro", cJogador, baralho, totem)
    
if venceu:
    #FASE 2
    print("Leshy - O ar úmido é tomado pelo cheiro fétido de mofo e morte, você caminha cautelosamente até entrar na... charneca.")
    carta = ""
    cartas = receber_cartas()
    baralho += montar_baralho(cartas)
    print(f"{len(cartas)} cartas foram adicionadas ao baralho")

    itens, totem = receberItens()
    print("Itens no inventario: " + ", ".join(itens))
    cJogador = calcular_coeficienteJogador(baralho, totem, itens)

    print("Pescador - Eu sou o Pescador. Quer pescar?")
    venceu2 = batalha("Pescador", cJogador, baralho, totem)

    if venceu2:
        #FASE 3
        print("Leshy - O alívio do ar fresco logo dá lugar a um arrepio álgido. Você escala até a... linha de neve.")
        carta = ""
        cartas = receber_cartas()
        baralho += montar_baralho(cartas)
        print(f"{len(cartas)} cartas foram adicionadas ao baralho")

        itens, totem = receberItens()
        print("Itens no inventario: " + ", ".join(itens))
        cJogador = calcular_coeficienteJogador(baralho, totem, itens)

        print("Comerciante - Vamos negociar.")
        venceu3 = batalha("Comerciante", cJogador, baralho, totem)

        if venceu3:
            print("Leshy - A luz cálida da cabana atravessa o denso nevoeiro... seus infortúnios acabam aqui.")