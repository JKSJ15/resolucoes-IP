def calcular_requisitos(nome, intensidade): 
    consumoMoli = 0
    consumoLotus = 0
    consumoCinzas = 0
    poderBase = 0

    if "lua" in nome.lower():
        consumoMoli = intensidade
        consumoLotus = 1
        poderBase = 10 * intensidade
    elif "sombras" in nome.lower():
        consumoLotus = intensidade
        consumoCinzas = 2
        poderBase = 12 * intensidade
    elif "familiar" in nome.lower():
        consumoMoli = 1
        consumoLotus = 1
        consumoCinzas = intensidade
        poderBase = 15 * intensidade

    return consumoMoli, consumoLotus, consumoCinzas, poderBase

def possui_ingredientes(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas):
    consumoMoli = moli >= custo_moli
    consumoLotus = lotus >= custo_lotus
    consumoCinzas = cinzas >= custo_cinzas
    return consumoMoli and consumoLotus and consumoCinzas

def conjurar_feitico(feitico, moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas, poder_base, nome, feitico_anterior):
    possui = possui_ingredientes(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas)
    sucesso = False
    sinergia = False
    poder_obtido = 0

    if possui: 
        sucesso = True
        moli -= custo_moli
        lotus -= custo_lotus
        cinzas -= custo_cinzas
        poder_obtido += poder_base

        if feitico > 0 and nome != feitico_anterior:
            poder_obtido += 5
            sinergia = True

        print(f"Melinoë conjurou {nome} e obteve {poder_obtido} de poder.")

        if sinergia:
            print("Sinergia lunar ativada! Selene concedeu 5 de poder extra.")
            print("Hécate: A luz de Selene responde à sua feitiçaria. Faça-a valer.")
        elif sucesso:
            if feitico == 0:
                print("Hécate: Foi para isto que treinamos todas essas noites, Melinoë.")
            else:
                print("Hécate: Disciplina, Melinoë. Uma bruxa vence antes mesmo de deixar a Encruzilhada.")
        
        print("Que assim seja!")
        return moli, lotus, cinzas, poder_obtido, nome
    else:
        print(f"Ingredientes insuficientes para conjurar {nome}.")
        print("Hécate: Intenção sem preparo não basta. Reúna os ingredientes e tente outra vez.")
        return moli, lotus, cinzas, 0, feitico_anterior

meta = (int(input()))
moli = (int(input()))
lotus = (int(input()))
cinzas = (int(input()))
quantidade_tentativas = (int(input()))

poder_total = 0
feitico_anterior = ""
for i in range(quantidade_tentativas):
    nome, intensidade = input().split(" ")
    intensidade = int(intensidade)
    consumo_moli, consumo_lotus, consumo_cinzas, poder_base = calcular_requisitos(nome, intensidade)
    moli, lotus, cinzas, poder_obtido, feitico_anterior = conjurar_feitico(i, moli, lotus, cinzas, consumo_moli, consumo_lotus, consumo_cinzas, poder_base, nome, feitico_anterior)
    poder_total += poder_obtido

print(f"\nPoder acumulado: {poder_total}")
print(f"Ingredientes restantes: {moli} moli, {lotus} lotus e {cinzas} cinzas.")

if meta <= poder_total:
    print("Melinoë está pronta para enfrentar Cronos.")
    print("Hécate: Você está pronta para partir. Lembre-se do que aprendeu na Encruzilhada — e retorne para nós.")
else:
    print("Melinoë precisa se preparar melhor antes de enfrentar Cronos.")
    print("Hécate: Cronos não terá piedade de você. Eu tampouco terei durante seu treinamento.")