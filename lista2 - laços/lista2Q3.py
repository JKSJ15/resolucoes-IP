print("Shrek achava que morar em um pântano afastado seria suficiente para manter as pessoas longe. Ele estava muito enganado.")
paciencia_shrek = int(input())
visitante = ""
assunto = ""
gasto_paciencia = 0
qtd_visitantes = 0
parar = False

while paciencia_shrek > 0 and not parar:
    visitante = str(input())
    if visitante.lower() == "ninguém":
        print("Ufa! Ninguém apareceu. Finalmente, um pouco de paz no pântano!")
        parar = True
    else:
        gasto_paciencia = int(input())
        if gasto_paciencia > paciencia_shrek:
            print("A paciência do Shrek acabou! Dê meia-volta antes que ele perca o controle!")
            parar = True
        if "burro" in visitante.lower() and not parar:
            qtd_visitantes += 1
            print("Burro?! Eu acabei de pedir um pouco de paz!")
            assunto = str(input())
            if "sanduíche" in assunto.lower():
                print("Ah, isso sim é um bom assunto!")
                gasto_paciencia //= 2
            elif "fiona" in assunto.lower():
                print("É o Burro! E, como sempre, ele só sabe falar da Fiona.")
            elif "pântano" in assunto.lower():
                print("Burro, isso é MEU pântano...")
            paciencia_shrek -= gasto_paciencia
        elif "gato de botas" in visitante.lower() and not parar:
            qtd_visitantes += 1
            paciencia_shrek -= gasto_paciencia
            print("O Gato de Botas chegou! Shrek já está de olho nas suas botas.")
        elif "pinóquio" in visitante.lower() and not parar:
            qtd_visitantes += 1
            paciencia_shrek -= gasto_paciencia
            print("Pinóquio chegou! Shrek espera que ele não esteja mentindo.")

        elif "lobo mau" in visitante.lower() and not parar:
            qtd_visitantes += 1
            paciencia_shrek -= gasto_paciencia
            print("Lobo Mau?! Shrek abriu a porta, mas já está se arrependendo!")
        else:
            if not parar:
                qtd_visitantes += 1
                paciencia_shrek -= gasto_paciencia
                print("Visitante desconhecido! Shrek não sabe quem você é, mas pode entrar por sua conta em risco.")
        if paciencia_shrek <= 0:
            print("A paciência do Shrek acabou! Dê meia-volta antes que ele perca o controle!")
            parar = True
print(f"Ao todo, {qtd_visitantes} visitantes passaram pelo pântano. Shrek sobreviveu a mais um dia!")