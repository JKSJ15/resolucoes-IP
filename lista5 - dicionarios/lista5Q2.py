dicionario = {"Vax":{}, "Pike":{}, "Grog":{}, "Percy":{}, "Scanlan":{}, "Vex":{}, "Keyleth":{}}

entrada = ""
nomeHeroi = ""
armaEnc = ""
poderArma = 0
while entrada != "FIM":
    entrada = input()
    if entrada != "FIM":
        #nome_do_heroi , arma_encontrada , poder_da_arma
        lista = entrada.split(",")
        nomeHeroi = lista[0].strip()
        armaEnc = lista[1].strip()
        poderArma = int(lista[2].strip())

        # validações
        if armaEnc == "Fenthras" and nomeHeroi == "Vex":
            print("Um arco mágico, capaz de controlar todos os elementos? isso é perfeito para mim querido!")
        elif armaEnc == "Manoplas de Titanstone" and nomeHeroi == "Grog":
            print("Estou maior agora, e pronto para entrar em fúria!")
        elif armaEnc == "Adaga Mágica" and nomeHeroi == "Vax":
            print("Uma arma dada pela própria rainha dos corvos, agora apenas preciso saber se isso é uma dádiva ou uma maldição.")
        elif armaEnc == "Caça Mitos" and nomeHeroi == "Scanlan":
            print("A espada lendária capaz de matar todos os Dragões... nas mãos do Scanlan?!")
        elif armaEnc == "Pináculo da Confluência" and nomeHeroi == "Keyleth":
            print("Com isso e meu aramenté completo, a natureza inteira estará sobre meu controle.")
        elif armaEnc == "The List" and nomeHeroi == "Percy":
            print("Não, ele novamente não, Orthax já me dominou uma vez, não posso deixar isso acontecer de novo.")
        elif armaEnc == "Placa do Mártir" and nomeHeroi == "Pike":
            print("Everlight, espero que um dia você me perdoe, mas não vou mais depender de você.")

        # atribuições
        inventarioHeroi = dicionario[nomeHeroi]
        inventarioHeroi.update({armaEnc: int(poderArma)})

# exibição
chaves = list(dicionario.keys())
for i in chaves:
    inventarioHeroi = dicionario[i]
    if len(inventarioHeroi) == 0:
        print(f"{i} não possui nenhuma arma.")
    else:
        chavesH = list(inventarioHeroi.keys())

        poderForte = 0
        armaForte = ""
        for j in chavesH:
            if inventarioHeroi[j] > poderForte:
                poderForte = inventarioHeroi[j]
                armaForte = j
        print(f"A arma mais forte de {i} é a {armaForte} com {poderForte} Pontos de Poder.")