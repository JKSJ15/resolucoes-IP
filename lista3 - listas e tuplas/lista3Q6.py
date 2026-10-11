matriz = []
parar = False

linhas = int(input())
colunas = int(input())

if linhas <= 0 or colunas <= 0:
    print("Dimensões do mapa inválidas!")
    parar = True

if parar == False:
    print("Avatar: A Lenda de Aang - Planejamento da Invasão!")
    print("Sokka: Mapeando os setores da Nação do Fogo...")

#criar matriz
i = 0
for i in range(linhas): #linhas
    if parar == False:
        linha = []

        for j in range(colunas): #colunas
            numero = int(input())
            linha.append(numero)

        matriz.append(linha)

#modificar matriz
n = len(matriz)
for j in range(n): # linhas
    for y in range(len(matriz[j])): #colunas
        if parar == False:
            if j == y:
                matriz[j][y] *= 2
            if linhas == colunas and j + y == n - 1:
                matriz[j][y] += 5

            if matriz[j][y] < 15:
                matriz[j][y] = 0
            if matriz[j][y] % 2 == 1:
                matriz[j][y] = matriz[j][y] + 1

#mostrar matriz
for j in range(n):  #linha
    for y in range(len(matriz[j])):  # coluna
        print(matriz[j][y], end="")

        if y < len(matriz[j]) - 1:
            print(" ", end="")
    print()

if parar == False:
    aliado = str(input())
    nivelEnergia = int(input())

#realizar acoes
i = 0
y = 0
soma = 0
if parar == False:  
    maiorValor = matriz[0][0]
else:
    maiorValor = 0
pares = 0
impares = 0
linhaMaior = 0
colunaMaior = 0
for j in range(n): # linhas
    for y in range(len(matriz[j])): #colunas
        if parar == False:
            if maiorValor < matriz[j][y]:
                maiorValor = matriz[j][y]
                linhaMaior = j
                colunaMaior = y

            soma += matriz[j][y]

            if matriz[j][y] % 2 == 0:
                pares += 1
            else:
                impares += 1

if parar == False:
    #relatorio    
    print(f"--- RELATÓRIO DO TÚNEL E AMEAÇAS ---\nSoma Total de Resistência: {soma}")
    print(f"Setor Mais Crítico: ({linhaMaior}, {colunaMaior}) com valor {maiorValor}")

    #validações
    if soma < 100:
        print("Sokka: O mapa revela poucas defesas inimigas!\nAang: Parece que o caminho está livre.")
        print("Katara: Conseguimos passar sem grandes problemas!\nEstratégia aprovada! O Avatar está pronto para a batalha.")
    elif 100 <= soma and soma < 200:
        print("Sokka: Atenção! Detectamos resistência nas defesas da Nação do Fogo.\nToph: Sinto muitas tropas pelo solo, mas podemos avançar com cuidado.")
        print("Aang: Então vamos atentos. A Equipe Avatar está pronta!\nEstratégia aprovada, mas a invasão será realizada com cautela.")
    else:
        print("Sokka: Alerta! As defesas inimigas são muito fortes!\nToph: A linha de defesa deles é densa demais para atravessarmos.")
        print("Aang: Então precisamos recuar e repensar nosso plano.\nAlerta vermelho: Nível de ameaça crítico! Invasão adiada.")

    if "Aang" in aliado:
        if soma <= nivelEnergia:
            print(f"{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!")
        else:
            print(f"{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...")
    elif "Katara" in aliado:
        if impares < pares:
            print(f"{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!")
        else:
            print(f"{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...")
    elif "Toph" in aliado:
        if maiorValor <= 50:
            print(f"{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!")
        else:
            print(f"{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...")
    elif "Sokka" in aliado:
        if linhas == colunas:
            print(f"{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!")
        else:
            print(f"{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...")