kit_rick = ["colt_357", "distintivo", "radio_comunicador", "cantil", "curativo"]
kit_michonne = ["katana", "amolador", "binoculo", "faixa_curativo", "mapa"]
kit_daryl = ["arco e flecha","flechas","faca_de_caca", "corda", "carne_seca"]
kit_carol = ["facao", "bomba_de_fumaca", "sangue_zumbi", "fosforos", "biscoito"]

kit  = ["taco_beisebol","besta","kit_medico", "feijao_enlatado", "walkie_talkie", "garrafa_agua","biscoito"]
kitSobrevivente = []
itens_para_carol = []

sobrevivente = input()
if "Rick" in sobrevivente:
    print("Um grande líder sempre ajuda sua equipe, Rick lhe dá uma lanterna para a noite")
    kit.append("lanterna")

    kit.remove("taco_beisebol")
    kit_rick.append("taco_beisebol")
    print(f"Kit atual sobrevivente: {kit}")

    kit_removido = kit[2:len(kit)]
    kit_rick = kit_rick + kit_removido
    kitSobrevivente = kit_rick
    del kit[2:len(kit)]

elif "Michonne" in sobrevivente:
    print("Michonne é uma ótima combatente, ela te dá uma arma para você não passar apertos.")
    kit.append("faca_afiada")

    print("Você usou o kit médico para socorrer Michonne!")
    kit.remove("kit_medico")
    print(f"Kit atual sobrevivente: {kit}")
    kit_removido = kit[2:len(kit)]
    kit_michonne = kit_michonne + kit_removido
    kitSobrevivente = kit_michonne
    del kit[2:len(kit)]

elif "Daryl" in sobrevivente:
    print("Daryl é um ótimo caçador. Ele te dá carne para comer na refeição")
    kit.append("carne")

    kit.remove("besta")
    kit.insert(1,"arco e flecha")
    kit_daryl.remove("arco e flecha")
    kit_daryl.insert(0,"besta")
    
    print(f"Kit atual sobrevivente: {kit}")
    print(f"Kit atual Daryl: {kit_daryl}")
    kit_removido = kit[2:len(kit)]
    kit_daryl = kit_daryl + kit_removido
    kitSobrevivente = kit_daryl
    del kit[2:len(kit)]

elif "Carol" in sobrevivente:
    print("Carol sabe como se esconder dos zumbis. Ela te dá uma ajuda.")
    kit.append("roupa_de_camuflagem")

    kit_carol.remove("bomba_de_fumaca")
    kit_carol.remove("sangue_zumbi")
    kit_carol.remove("fosforos")
    itens_para_carol = kit[2:4]
    kit_carol = kit_carol+itens_para_carol
    del kit[2:4]

    kit_removido = kit[2:len(kit)]
    kit_carol = kit_carol + kit_removido
    kitSobrevivente= kit_carol
    del kit[2:len(kit)]

print("Agora com as costas mais leves, podemos continuar com a nossa caminhada\n")
print("Finalmente chegamos em Alexandria!\n")
print(f"Ufa, podemos ficar aqui por um tempo,{sobrevivente}\n")
print(f"Kit do sobrevivente: {kit}\n")
print(f"Kit do {sobrevivente}: {kitSobrevivente}")