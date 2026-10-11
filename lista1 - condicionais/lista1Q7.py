print("Depois que a Série A e a Libertadores ficaram só no sonho do Santa, Byte pendura a chuteira de ídolo tricolor e parte pro interior: começa a Excursão Interiorana em busca do time da sua vida!")

visitas_contaram = 0
gostou = 0
nao_gostou = 0

foi_catende = False
foi_palmares = False

caracteristica1 = str(input().strip().lower())
veredito1 = str(input().strip().lower())

if "maior usina de açúcar e álcool da américa latina" in caracteristica1 or "catende" in caracteristica1:
    print("Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar.")
    foi_catende = True
elif "terra dos poetas" in caracteristica1 or "ascenso ferreira" in caracteristica1 or "palmares" in caracteristica1:
    print("Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso.")
    foi_palmares = True
elif "carcará" in caracteristica1:
    print("Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!")
    visitas_contaram += 1
elif "patativa" in caracteristica1:
    print("Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!")
    visitas_contaram += 1
elif "azulão" in caracteristica1:
    print("Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!")
    visitas_contaram += 1
elif "fruticultura" in caracteristica1:
    print("Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!")
    visitas_contaram += 1
elif "pássaro preto" in caracteristica1:
    print("Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!")
    visitas_contaram += 1

if veredito1 == "gostou":
    print("Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.")
    gostou += 1
else:
    print("Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.")
    nao_gostou += 1

caracteristica2 = input().strip().lower()
veredito2 = input().strip().lower()

if "maior usina de açúcar e álcool da américa latina" in caracteristica2 or "catende" in caracteristica2:
    print("Catende!!! Aqui já rodou a maior usina de açúcar e álcool da América Latina, Byte sente o orgulho no ar.")
    foi_catende = True
elif "terra dos poetas" in caracteristica2 or "ascenso ferreira" in caracteristica2 or "palmares" in caracteristica2:
    print("Palmares, a Terra dos Poetas! Berço de nomes como Ascenso Ferreira, aqui até o futebol merece um verso.")
    foi_palmares = True
elif "carcará" in caracteristica2:
    print("Carcará no peito! Essa é terra de Salgueiro, o primeiro clube do interior a ser campeão pernambucano, Byte sente o chamado do Sertão!")
    visitas_contaram += 1
elif "patativa" in caracteristica2:
    print("Show da Patativa! Caruaru e o Central esperam Byte de braços abertos, direto da maior feira a céu aberto do mundo!")
    visitas_contaram += 1
elif "azulão" in caracteristica2:
    print("Ar puro de serra! O Azulão de Bonito, sensação recente do Pernambucano, pode ser o novo lar de Byte!")
    visitas_contaram += 1
elif "fruticultura" in caracteristica2:
    print("Margens do Velho Chico! Petrolina, a maior cidade do interior, com direito a manga, uva e muita irrigação, chama Byte pro time!")
    visitas_contaram += 1
elif "pássaro preto" in caracteristica2:
    print("Pertinho de casa! O Pássaro Preto, orgulhosamente um dos times mais folclóricos do planeta, também está de olho em Byte!")
    visitas_contaram += 1

if veredito2 == "gostou":
    print("Aquele cheirinho de interior fisgou o faro do Byte! Visita gostosa, mas ele quer conhecer mais um pouco antes de assinar.")
    gostou += 1
else:
    print("Byte torceu o focinho dessa vez... não rolou clima pra ficar por aqui.")
    nao_gostou += 1

if foi_catende and foi_palmares:
    print("Catende e Palmares na excursão? Aí sim Byte tá garimpando ouro puro da Zona da Mata Sul! Pena que acabou por aqui.")

print()
print("RELATÓRIO DA EXCURSÃO SERTANEJA DO BYTE:")
print(f"- Visitas que contaram: {visitas_contaram}")
print(f"- Gostou: {gostou}")
print(f"- Não gostou: {nao_gostou}")
print()
print("E assim termina a Excursão Interiorana de Byte em Pernambuco. Anotar tudo isso na unha, sem laço nem lista, dá um trabalhão! Nas próximas férias, Byte espera que a molecada já saiba de laços, listas e funções pra dar conta do recado com estilo :)")