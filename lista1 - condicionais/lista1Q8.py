print("Byte: Au! Vou conseguir esse ovo!!")
fase1 = str(input())

nivelPerigo = 0
minutos = len(fase1) * 5
estrutura = ""
camas = False
enfrentou_troia = False
lingotes_ouro = False
morto = False

if fase1.isupper():
    nivelPerigo += 30  
else:
    nivelPerigo += 10

if "monstros" in fase1.lower():
    print("Você não pode dormir agora, há monstros por perto.")
    nivelPerigo += 25
    minutos += 20
    if "4" in fase1:
        print("Byte desbloqueou a conquista: [Caçador de Monstros]")
        nivelPerigo *= 2

if "ferro" in fase1.lower():
    print("Byte desbloqueou a conquista: [A Idade do Ferro]")
    nivelPerigo -= 15
    nivelPerigo = max(0, nivelPerigo)
    minutos += 5

if "diamante" in fase1.lower():
    if "ferro" in fase1.lower():
        print("Byte desbloqueou a conquista: [Diamantes!]")
        nivelPerigo -= 40
        nivelPerigo = max(0, nivelPerigo)
    else:
        minutos += 15

if "ouro" in fase1.lower():
    if "ferro" in fase1.lower():
        lingotes_ouro = True
        minutos += 10
    else:
        minutos += 5

if "estrutura" in fase1.lower():
    estrutura = str(input())
    if "vila" in estrutura.lower():
        print("Byte desbloqueou a conquista: [Negócio Fechado!]")
        camas = True
        minutos += 10
    if "templo" in estrutura.lower():
        nivelPerigo += 100
    if "mansao" in estrutura.lower():
        if nivelPerigo > 100:
            print("Byte desbloqueou a conquista: [À beira da Morte]")
        nivelPerigo -= 150
        nivelPerigo = max(0, nivelPerigo)
        minutos += 40
    if "camara" in estrutura.lower():
        print("Byte desbloqueou a conquista: [Minecraft: Jogos Vorazes]")
        nivelPerigo += 50
        minutos += 60

if nivelPerigo <= 100:
    print("Byte: Ufa, finalmente acabei, demorei apenas {} minutos, vamos ao Nether!".format(minutos))

    if "portal" not in estrutura.lower():
        print("Byte desbloqueou a conquista: [Entrando numa fria]")
        minutos += 5

    print("Byte desbloqueou a conquista: [O buraco é mais embaixo]")
    nivelPerigo += 30

    n1 = float(input())
    n2 = float(input())
    soma = n1 + n2

    if int(soma) != soma:
        if lingotes_ouro is True:
            print("Byte desbloqueou a conquista: [Meu precioso!]")
            nivelPerigo += 10
        else:
            nivelPerigo += 20
            minutos += 30

    resultado_blaze = str(input())

    if resultado_blaze.isnumeric():
        resultado_blaze = int(resultado_blaze)
        if 1 <= resultado_blaze <= 12:
            minutos += 20
        elif resultado_blaze > 12:
            minutos += 10
        else:
            minutos += 30
            nivelPerigo += 40
    else:
        minutos += 30
        nivelPerigo += 40

    if nivelPerigo <= 100:
        nivelPerigo -= 20
        nivelPerigo = max(0, nivelPerigo)

        x = int(input())
        z = int(input())

        distancia = int(((100 - x) ** 2 + (200 - z) ** 2) ** 0.5)
        print(f"Byte: Estou a {distancia} blocos da Stronghold!")
        minutos += distancia * 2

        nivelPerigo += 30
        horas = int(minutos / 60)

        if horas > 5:
            print("Troia desbloqueou a conquista: [Liberte o End]")
            print("Byte desbloqueou a conquista: [É o fim?]")
            print("Byte: auu.... Não consegui pegar o ovo...")
            enfrentou_troia = True

        elif camas is True:
            print("Byte desbloqueou a conquista: [É o fim?]")
            print("Byte: Como eu amo o [Design Intencional do Jogo]!")
            nivelPerigo -= 30
            nivelPerigo = max(0, nivelPerigo)
            print("Byte desbloqueou a conquista: [A nova geração]")
            print("Byte: Aauauau! O ovo é meu! que rolem os créditos!")

        elif horas >= 3 and horas < 5:
            print("Troia desbloqueou a conquista: [É o fim?]")
            print("Byte desbloqueou a conquista: [É o fim?]")
            enfrentou_troia = True
            nivelPerigo += 10

            flechas = int(input())
            alvos = int(input())

            if alvos == 1 and flechas == 1:
                print("Byte: Uma flecha, Uma chance.")
            elif alvos == 1:
                print("Byte: Troia já destruiu todos os cristais, agora é só o Dragão...")

            divisao = alvos / flechas
            divisaoExata = flechas % alvos == 0
            if divisao > 0 and divisaoExata:
                minutos += 10
                print("Byte desbloqueou a conquista: [Liberte o End]")
                if nivelPerigo <= 100:
                    print("Byte desbloqueou a conquista: [A nova geração]")
                    print("Byte: Aauauau! O ovo é meu! que rolem os créditos!")
                else:
                    morto=True
            else:
                minutos += 20
                print("Byte: Droga! Não tenha flechas suficientes, Troia vai ganhar...")
                print("Byte: auu.... Não consegui pegar o ovo...")
        else:
            minutos += 5
            print("Byte desbloqueou a conquista: [É o fim?]")
            print("Byte desbloqueou a conquista: [Liberte o End]")
            print("Byte desbloqueou a conquista: [A nova geração]")
            print("Byte: Aauauau! O ovo é meu! que rolem os créditos!")

    else:
        morto = True
else:
    morto = True

if morto is True:
    print("Byte foi morto.")
    print("Byte: auu.... Não consegui pegar o ovo...")

print("\n🚨Avaliação de nível de perigo: ", end="")

if nivelPerigo == 100 or enfrentou_troia is True:
    print("Odisseia de Byte.")
elif nivelPerigo < 30:
    print("Passeio no Parque.")
elif nivelPerigo >= 30 and nivelPerigo < 70:
    print("Jornada Complicada.")
elif nivelPerigo >= 70 and nivelPerigo < 100:
    print("Aventura Perigosa.")
elif nivelPerigo > 100:
    print("Letal.")

horas = minutos // 60
resto_min = minutos % 60
print(f"\nTimer: {horas} h e {resto_min} minutos")