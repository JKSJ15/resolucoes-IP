temperaturas = []
pulsos = []
trocas = []
presoes = []
tamanho_amostra = 0

print("Espaço: a fronteira final. Estas são as viagens da nave estelar Enterprise…")
print("Sua missão de cinco anos: explorar novos mundos, procurar novas vidas e novas civilizações, audaciosamente indo aonde nenhum homem jamais esteve.")
print("Dr. McCoy: Eu sou um médico, não um matemático. Mas tenho que fazer o que precisa ser feito.")
print("=====")

while tamanho_amostra < 5 or tamanho_amostra > 12:
    tamanho_amostra = int(input())
    if tamanho_amostra < 5 or tamanho_amostra > 12:
        print("Dr. McCoy: Esse número não é ideal, é possível trazer uma amostra de 5 a 12 indivíduos?")

print(f"Dr. McCoy: Certo, {tamanho_amostra} indivíduos. É um número bom.")
print("=====")

i = 0
for i in range(tamanho_amostra):
    linha = input()

    partes = linha.split(" - ")
    temp = float(partes[0].split()[0])
    temperaturas.append(temp)
    pulso = float(partes[1].split()[0])
    pulsos.append(pulso)
    troca = float(partes[2].split()[0])
    trocas.append(troca)
    pressao = float(partes[3].split()[0])
    presoes.append(pressao)

print("Relatório de dados da amostra:")
temperaturas.sort(); pulsos.sort(); trocas.sort(); presoes.sort()

tamanhoTemp = len(temperaturas)
tamanhoMeio = int((tamanhoTemp//2))
if tamanhoTemp %2 == 0: 
    medianaTemp = round((temperaturas[tamanhoMeio-1] + temperaturas[tamanhoMeio])/2,1)
else:
    medianaTemp = round(temperaturas[tamanhoMeio],1)
print(f"Temperatura: {temperaturas}")
print(f"Mediana: {medianaTemp}")

tamanhoPulsos = len(pulsos)
tamanhoMeio = int((tamanhoPulsos//2))
if tamanhoPulsos %2 == 0: 
    medianaPulsos = round((pulsos[tamanhoMeio-1] + pulsos[tamanhoMeio])/2,1)
else:
    medianaPulsos = round(pulsos[tamanhoMeio],1)
print(f"Frequência de pulso fluido: {pulsos}")
print(f"Mediana: {medianaPulsos}")

tamanhoTrocas = len(trocas)
tamanhoMeio = int((tamanhoTrocas//2))
if tamanhoTrocas % 2 == 0:
    medianaTrocas = round((trocas[tamanhoMeio-1] + trocas[tamanhoMeio]) / 2, 1)
else:
    medianaTrocas = round(trocas[tamanhoMeio], 1)

print(f"Frequência de troca gasosa: {trocas}")
print(f"Mediana: {medianaTrocas}")

tamanhoPressoes = len(presoes)
tamanhoMeio = int((tamanhoPressoes//2))
if tamanhoPressoes %2 == 0: 
    medianaPressoes = round((presoes[tamanhoMeio-1] + presoes[tamanhoMeio])/2,1)
else:
    medianaPressoes = round(presoes[tamanhoMeio],1)
print(f"Pressão interna de homeostase: {presoes}")
print(f"Mediana: {medianaPressoes}")
print("=====")

print("Dr. McCoy: Agora irei medir os sinais do paciente.")
print("=====")

linha = input()
partes = linha.split(" - ")
tempP = float(partes[0].split()[0])
pulsoP = float(partes[1].split()[0])
trocaP= float(partes[2].split()[0])
pressaoP = float(partes[3].split()[0])

criticos = 0
if tempP < min(temperaturas) or tempP > max(temperaturas): criticos += 1
if pulsoP < min(pulsos) or pulsoP > max(pulsos): criticos += 1
if trocaP < min(trocas) or trocaP > max(trocas): criticos += 1
if pressaoP < min(presoes) or pressaoP > max(presoes): criticos += 1

if criticos >= 2:
    avaliacao = "Alerta Crítico"  
else:
    avaliacao = "Estável"

difTemp = round(tempP - medianaTemp, 1)
difPulso = round(pulsoP - medianaPulsos, 1)
difTroca = round(trocaP - medianaTrocas, 1)
difPressao = round(pressaoP - medianaPressoes, 1)

print("Relatório final:")
print(f"Temperatura do paciente: {tempP}")
print(f"Diferença para a mediana: {difTemp}")
print(f"Frequência de pulso fluido do paciente: {pulsoP}")
print(f"Diferença para a mediana: {difPulso}")
print(f"Frequência de troca gasosa: {trocaP}")
print(f"Diferença para a mediana: {difTroca}")
print(f"Pressão interna de homeostase: {pressaoP}")
print(f"Diferença para a mediana: {difPressao}")
print(f"Quantidade de sinais críticos encontrados: {criticos}")
print(f"Avaliação final: {avaliacao}")
print("=====")
print("Dr. McCoy: Certo, agora sei o que fazer.")