ameaca = ""
registro = []

while not "FIM" in ameaca:
    ameaca = input()
    if not "FIM" in ameaca:
        partes = ameaca.split(",")
        danoBase = float(partes[2])
        inteligencia = int(partes[3])
        fatorCaos = float(partes[4])

        nivel_inicial = danoBase + (inteligencia * fatorCaos)
        if partes[1] == "Enclave":
            nivel_ameaca = nivel_inicial - (nivel_inicial * 0.15)
        else:
            nivel_ameaca = nivel_inicial

        ameacas = (-nivel_ameaca, partes[0], partes[1])
        registro.append(ameacas)
        
novoRegistro = registro[0:len(registro)]

lista_faccoes = []
for i in range(len(registro)):
    faccao = registro[i][2]
    lista_faccoes.append(faccao)

novoNovoRegistro = []
for nivel_neg, nome, faccao in novoRegistro:
    nivel_original = -nivel_neg
    frequencia_faccao = lista_faccoes.count(faccao)
    nivel_ajustado = nivel_original + (nivel_original * 0.05 * (frequencia_faccao - 1))    
    novoNovoRegistro.append((-nivel_ajustado, nome, faccao))

novoNovoRegistro.sort()
suporte = []
for j in range(len(novoNovoRegistro)):
    if j+1 > len(novoNovoRegistro):
        if novoNovoRegistro[j][0] == novoNovoRegistro[j+1][0]: # nivel ajustado
            # menor nome em ordem alfabetica
            if novoNovoRegistro[j][1] < novoNovoRegistro[j+1][1]:
                suporte = novoNovoRegistro[i]
                novoNovoRegistro[j] = novoNovoRegistro[j+1]
                novoNovoRegistro.insert(j+1, suporte)

            elif novoNovoRegistro[j][1] == novoNovoRegistro[j+1][1]: # continua empatado
                # menor faccao
                if novoNovoRegistro[j][2] < novoNovoRegistro[j+1][2]:
                    suporte = novoNovoRegistro[j]
                    novoNovoRegistro[j] = novoNovoRegistro[j+1]
                    novoNovoRegistro.insert(j+1, suporte)

zona_prioritaria = novoNovoRegistro[:min(3, len(novoNovoRegistro))]
zona_acompanhamento = novoNovoRegistro[min(3, len(novoNovoRegistro)):]

print(zona_prioritaria)