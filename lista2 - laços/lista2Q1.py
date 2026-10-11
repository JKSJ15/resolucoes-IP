print("Parabéns formandos! E agora iniciaremos sua carreira nas indústrias Honex.")
n = int(input())

vagas_unicas = ""
repeticoes = 0
qtd_unicas = 0

for i in range(n):
    vaga = input()
    if vaga in vagas_unicas:
        repeticoes += 1
    else:
        if vagas_unicas == "":
            vagas_unicas = vaga
        else:
            vagas_unicas += " - "+vaga
        qtd_unicas += 1

print(vagas_unicas)
print(f"Quantidade de cargos repetidos: {repeticoes}")

if qtd_unicas > repeticoes:
    print("Pelo menos Barry tem opções!")
else:
    print("Mais do mesmo. Barry será apenas uma engrenagem na máquina de mel.")
