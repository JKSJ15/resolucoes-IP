def contar_variacoes(fraseP, variacoesP):
    qnt = 0
    for i in variacoesP:
        qnt += fraseP.count(i)
    return qnt

variacoes = {
    "a": "aáàâãäAÁÀÂÃÄ",
    "e": "eéèêëEÉÈÊË",
    "i": "iíìîïIÍÌÎÏ",
    "o": "oóòôõöOÓÒÔÕÖ",
    "u": "uúùûüUÚÙÛÜ"
}
censoA = "aáàâãäAÁÀÂÃÄ" 
censoE = "eéèêëEÉÈÊË" 
censoI ="iíìîïIÍÌÎÏ" 
censoO ="oóòôõöOÓÒÔÕÖ" 
censoU ="uúùûüUÚÙÛÜ"

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_validas = alfabeto + censoA + censoE + censoI + censoO + censoU

# entradas
frase = input()
animago = input().strip()

# censo
resultado = []
vistos = ""
for caractere in frase:
    quant = 0
    if caractere in letras_validas and caractere.lower() not in vistos and caractere.upper() not in vistos:
        if caractere.lower() in variacoes:
            variacoesCaractere = variacoes[caractere.lower()]
            quant = contar_variacoes(frase, variacoesCaractere)
            caractere = caractere.lower()
            vistos += variacoesCaractere

        elif caractere in censoA and "a" not in vistos and "A" not in vistos:
            quant = contar_variacoes(frase, censoA)
            caractere = "a"
            vistos += censoA

        elif caractere in censoE and "e" not in vistos and "E" not in vistos:
            quant = contar_variacoes(frase, censoE)
            caractere = "e"
            vistos += censoE

        elif caractere in censoI and "i" not in vistos and "I" not in vistos:
            quant = contar_variacoes(frase, censoI)
            caractere = "i"
            vistos += censoI

        elif caractere in censoO and "o" not in vistos and "O" not in vistos:
            quant = contar_variacoes(frase, censoO)
            caractere = "o"
            vistos += censoO

        elif caractere in censoU and "u" not in vistos and "U" not in vistos:
            quant = contar_variacoes(frase, censoU)
            caractere = "u"
            vistos += censoU

        else:
            quant = frase.count(caractere.upper())
            quant += frase.count(caractere.lower())
            caractere = caractere.lower()

        resultado.append(str(quant) + caractere.lower())
        vistos += caractere

# ordenação
for i in range(len(resultado)):
    for j in range(len(resultado) - 1 - i):
        if int(resultado[j][:-1]) < int(resultado[j + 1][:-1]):
            resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]

# interrogatório
total = 0
ocorrencias = {animago: {}}

# animago é vogal?
if animago in variacoes:
    letras = variacoes[animago]

# animago é consoante?
else:
    letras = animago + animago.upper()

# contagem das variantes na frase
vistos2 = ""
for letra in frase:
    if animago in variacoes and letra not in vistos2:
        letras = variacoes[animago]
        if letra in letras:
            qtd = frase.count(letra)
            if qtd > 0:
                ocorrencias[animago][letra] = qtd
                total += qtd
        vistos2 += letra
    else:
        letras = animago + animago.upper()
        if letra in letras and letra not in ocorrencias[animago] and letra not in vistos2:
            qtd = frase.count(letra)
            if qtd > 0:
                ocorrencias[animago][letra] = qtd
                total += qtd
        vistos2 += letra

qtd_variacoes = len(ocorrencias[animago])

# verificação da maior ocorrência
variacao = ""
qtd_variacao = 0

for letra in ocorrencias[animago]:
    if ocorrencias[animago][letra] >= qtd_variacao:
        qtd_variacao = ocorrencias[animago][letra]
        variacao = letra

# exibições
print(" ".join(resultado))
print(f"Total de ocorrências: {total}")
print(f"Quantidade de variações: {qtd_variacoes}")
print(f"Variação mais frequente: {variacao} ({qtd_variacao})")