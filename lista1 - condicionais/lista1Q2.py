print("Byte recebeu um novo chamado! Preparando-se para a aventura...")
energia = int(input())
petiscos = int(input())
agua = int(input())
bateria_coleira = int(input())
gps = str(input())
bolinha = str(input())
chuva = str(input())
temperatura = int(input())
intensidade_sinal = int(input())

nivelPreparo = 0

if energia >= 70:
    print("Byte está cheio de energia!")
    nivelPreparo +=2
elif energia < 30:
    print("Byte está muito cansado... A missão ficou mais difícil.")
    nivelPreparo -= 2
if petiscos >= 2 and agua >= 1:
    print("Suprimentos preparados!")
    nivelPreparo += 2
if bateria_coleira >= 50 and "sim" in gps.lower():
    print("Coleira tecnológica preparada!")
    nivelPreparo  += 2
if bateria_coleira <= 20:
    print("A bateria da coleira está crítica! Isso pode atrapalhar a missão.")
    nivelPreparo -= 1
if "sim" in bolinha.lower() or petiscos >= 4:
    print("Byte está ainda mais animado para a aventura!")
    nivelPreparo += 1
if "sim" in chuva.lower() or temperatura > 32:
    print("O clima não está ajudando... Isso vai dificultar a missão.")
    nivelPreparo -= 2
if intensidade_sinal >= 70:
    print("O sinal está forte! Há algo estranho por perto...")
    nivelPreparo += 1

print()
print(f"Nível de preparo: {nivelPreparo}")

if nivelPreparo >= 5:
    print("Byte está pronto! A nova aventura começa agora!")
else:
    print("Byte ainda não está pronto. Melhor se preparar um pouco mais!")