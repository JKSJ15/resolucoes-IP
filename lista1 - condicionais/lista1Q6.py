login = str(input())
password = str(input())

print("Byte irá julgar a sua senha.")

hasDigit = "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password
hasSymbol = "@" in password or "_" in password or "&" in password or "%" in password or "#" in password
justWords = (not hasDigit) and (not hasSymbol)

if len(password) < 8 or " " in password or justWords or password.isnumeric():
    print("Essa senha nem chega perto do que eu aceito. Tente de novo.")
else:
    print("Vamos fazer a contagem dos pontos.")

    securityPoints = 0
    warningPoints = 0

    if len(password) > 11:
        securityPoints += len(password) - 11

    if password != password.upper() and password != password.lower():
        securityPoints += 5

    if "@" in password:
        securityPoints += 1

    if "_" in password:
        securityPoints += 1

    if "&" in password:
        securityPoints += 1

    if "%" in password:
        securityPoints += 1

    if "#" in password:
        securityPoints += 1

    if len(password) > 14:
        print("Que senha grande! Não seria difícil esquecer dela.")

    if login.lower() in password.lower():
        warningPoints += 10
        print("Olha o que eu encontrei aqui, não deixarei isso passar tão fácil.")

    finalPoints = securityPoints - warningPoints

    if finalPoints < 1:
        print("Infelizmente terá que mudar sua senha, é para o seu bem.")
        print(f"Melhore sua senha em {1 - finalPoints} ponto(s) e ela será suficiente.")

    elif finalPoints < 11:
        print("Pode manter a sua senha, ela parece adequada.")

    else:
        print("Parabéns! Nem o maior hacker do mundo encontraria uma senha assim.")