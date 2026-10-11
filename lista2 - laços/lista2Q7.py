papaiHp = 100
danoBreu = 15
custo = 10
fatorContinente = 0
modificadorPais = 0
parar = False
totalPresentes = 0
totalCarvao = 0
custoGlobal = 0
comportamento = 0
presenteStreak = 0
carvaoStreak = 0
localidade = ""
nome_crianca_ou_evento = ""


while "FIM" != localidade and papaiHp > 0 and parar == False:
    localidade = input()
    if "FIM" == localidade:
        parar = True
    else:
        continente = str(input())
        pais = str(input())

        if pais == "Brasil":
            modificadorPais = 1.10
        elif pais == "EUA":
            modificadorPais = 1.15
        elif pais == "China":
            modificadorPais = 1.20
        elif pais == "Canadá" or pais == "Canada":
            modificadorPais = 1.25
        elif pais == "Rússia" or pais == "Russia":
            modificadorPais = 1.30
        else:
            modificadorPais = 1.00

        if continente == "Europa":
            fatorContinente = 1.0
        elif continente == "Oceania":
            fatorContinente = 2.0
        elif continente == "América" or continente == "America":
            fatorContinente = 3.0
        elif continente == "África" or continente == "Africa":
            fatorContinente = 4.0
        elif continente == "Ásia" or continente == "Asia":
            fatorContinente = 5.0
        else:
            fatorContinente = 1.0

        custo = 10
        custoLocal = 0.0
        pararLocal = False
        sobrecarga = False
        nome_crianca_ou_evento = ""

        while "FIM_LOCAL" != nome_crianca_ou_evento and not parar and not pararLocal:
            nome_crianca_ou_evento = str(input())
            if "FIM_LOCAL" == nome_crianca_ou_evento:
                pararLocal = True
                print(f"Localidade {localidade} finalizada. Custo logístico: {custoLocal:.2f}")
            elif "Breu" == nome_crianca_ou_evento:
                print("Alerta! Breu atacou a entrega!")
                breuHp = 50
                iniciativa = input()
                vez = iniciativa

                while papaiHp > 0 and breuHp > 0:
                    acao = input()
                    if vez == "Noel":
                        breuHp -= 20
                        vez = "Breu"
                    else:
                        papaiHp -= danoBreu
                        vez = "Noel"

                if papaiHp > 0 and breuHp <= 0:
                    print("Noel repeliu a emboscada e as entregas continuam!")
                elif papaiHp <= 0:
                    pararLocal = True
                    parar = True
            else:
                crianca = nome_crianca_ou_evento
                comportamentoValido = False
                comportamento = 0

                while not comportamentoValido:
                    comportamento = int(input())
                    if comportamento < 0 or comportamento > 100:
                        print("Pontuação inválida, insira novamente.")
                    else:
                        comportamentoValido = True

                custoCrianca = custo * fatorContinente * modificadorPais
                custoLocal += custoCrianca
                custoGlobal += custoCrianca

                if comportamento >= 70:
                    print(f"{crianca} foi uma boa criança este ano e receberá um presente!")
                    totalPresentes += 1
                    presenteStreak += 1
                    carvaoStreak = 0

                    if presenteStreak == 3:
                        papaiHp += 10
                        papaiHp = min(papaiHp, 100)
                        print("A fé das crianças fortalece a magia! Noel recuperou 10 de HP.")
                        presenteStreak = 0

                else:
                    print(f"{crianca} não se comportou bem e receberá carvão.")
                    totalCarvao += 1

                    carvaoStreak += 1
                    presenteStreak = 0
                    if carvaoStreak == 3:
                        danoBreu += 5
                        print(f"O medo e a descrença alimentam as sombras... O dano de Breu aumentou para {danoBreu}!")
                        carvaoStreak = 0

                if custoLocal > 100.0 and not sobrecarga:
                    print("O trenó está sobrecarregado pela magia! Custos base aumentados.")
                    sobrecarga = True
                    custo = 15

if papaiHp > 0:
    print(f"Noite concluída com sucesso! Presentes: {totalPresentes} | Carvão: {totalCarvao}")
    print(f"Custo logístico total: {custoGlobal:.2f}")
    print(f"HP final do Noel: {papaiHp}")
else:
    print("O HP de Noel chegou a zero! O Breu venceu a batalha... O Natal das crianças foi arruinado.")