print("--- FASE 1: A VARREDURA ---")
linhas = int(input())
print("Lisbon: Jane, focamos as buscas no quadrante delimitado.")
matriz = []
colunas = 0
auxiliar = []
elemento = ""

for i in range(linhas):
    elemento = input()
    matriz.append(elemento.split(", "))
    colunas = len(elemento.split(", "))

inteiros = input()
auxiliar = inteiros.split(" ") 

linha_inicio = int(auxiliar[0]) 
linha_fim = int(auxiliar[1])  
coluna_inicio = int(auxiliar[2])  
coluna_fim = int(auxiliar[3])  

sub_matriz = []
for j in range(linha_inicio, linha_fim):
    linhaSub = []
    for k in range(coluna_inicio, coluna_fim):
        linhaSub.append(matriz[j][k])
    sub_matriz.append(linhaSub)
    print(sub_matriz[-1])

sangues = 0
armas = 0
auxiliar1 = 0
smiley = False
for l in range(len(sub_matriz)):
    sangues += sub_matriz[l].count("Sangue")
    armas += sub_matriz[l].count("Arma")
    auxiliar1 += sub_matriz[l].count("Smiley")
    if auxiliar1 > 0:
        smiley = True
simNao = ""
if smiley:
    simNao = "Sim"
else:
    simNao = "Nao"
print(f"Evidencias encontradas: Sangue ({sangues}), Arma ({armas}). Smiley ({simNao})")
print()

print("--- FASE 2: A MATRIZ DE EVIDÊNCIAS ---")
evidencia = input().split(" ")
lMatrizEvidencia = int(evidencia[0])
cMatrizEvidencia = int(evidencia[1])

print("Patrick Jane: Às vezes, a verdade está escondida bem diante dos nossos olhos.")
matrizEvidencia = []
for n in range(lMatrizEvidencia):
    linha = input()
    matrizEvidencia.append(linha.split(" "))

limiar = int(input()) 
matriz_binaria = matrizEvidencia.copy()
for o in range(len(matriz_binaria)):
    for p in range(len(matriz_binaria[o])):
        if int(matriz_binaria[o][p]) >= limiar:
            matriz_binaria[o][p] = 1
        else:
            matriz_binaria[o][p] = 0 
    print(" ".join(str(num) for num in matriz_binaria[o]))

linh = 0
colun = 0
assinatura = False
sorriso = [
           [1, 1, 0, 1, 1],
           [1, 0, 0, 0, 1],
           [0, 1, 1, 1, 0]
           ]

for q in range(lMatrizEvidencia-2):
    for r in range(cMatrizEvidencia-4):
        igual = True
        for y in range(3):
            for z in range(5):
                if matriz_binaria[q + y][r + z] != sorriso[y][z]:
                    igual = False
        if igual:
            assinatura = True
            linh = q
            colun = r

if assinatura == False:
    print("Patrick Jane: Nada aqui parece familiar.")
    print()
else:
    print("Patrick Jane: Eu conheço esse sorriso.")
    print("RED JOHN DEIXOU UMA ASSINATURA!")
    print(f"ASSINATURA ENCONTRADA EM [{linh}][{colun}]")
    print()

if smiley or assinatura:
    print("--- FASE 3: A MENSAGEM ---")

    indice = 0
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    sequencia = input()
    seq = sequencia.split(" ")
    lista_caracteres = []

    lista_caracteres = [alfabeto[(int(x) // 2) % 27] if int(x) % 2 == 0 else alfabeto[(int(x) * 3 + 1) % 27] for x in seq]
    mensagem = "".join(lista_caracteres)

    print(f'Mensagem decodificada: "{mensagem}"')
    print("Jane: Ele acha que é mais esperto que eu. Nós vamos pegá-lo.")
else:
    print("--- FASE 3: O CÓDIGO ---")
    print("Patrick Jane: Vamos ver o que ele quis dizer dessa vez.")
    cod = input()
    codInv = cod[::-1]
    caracteresPares = []
    stringImpares = ""
    msgDec = ""

    for t in range(len(codInv)):
        if t % 2 == 0:
            ch = codInv[t]
            if ch.isupper():
                msgDec += ch.lower()
            elif ch.islower():
                msgDec += ch.upper()
            else:
                msgDec += ch
            

    grauObcessao = msgDec.lower().count('j')

    print("MENSAGEM DECODIFICADA!")
    print(f"Patrick Jane: '{msgDec}'...")
    print("Patrick Jane: Esse caso acabou de dar uma reviravolta interessante.")
    print(f"Grau de Obsessão: {grauObcessao} aparição(ões) da letra J na mensagem.")
    print("--- CASO ENCERRADO (por enquanto...) ---")