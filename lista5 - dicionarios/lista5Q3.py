# calculo de dano
def calcularDanoHeroi(arma, heroiP):
   if arma == "Espada Sagrada":
       print(f"{heroiP} brandiu {arma} contra o Rei Demônio e causou 15 pontos de dano!")
       return 15
   elif arma == "Arco Lendário":
       print(f"{heroiP} brandiu {arma} contra o Rei Demônio e causou 20 pontos de dano!")
       return 20
   elif arma == "Cajado Magistral":
       print(f"{heroiP} brandiu {arma} contra o Rei Demônio e causou 25 pontos de dano!")
       return 25 
   else:
       print("A arma do herói não possui poder suficiente para atravessar a aura sombria do Rei Demônio!")
       return 0

# início
dicionario = {}
print("As sombras avançam sobre o Reino Celeste... É chegada a hora de reunir os heróis dispostos a enfrentar o Rei Demônio!")

# atribuição de herois
heroi = ""
vidaHeroi = 0
agilHeroi = 0
armaHeroi = ""
while heroi != "FIM":
   heroi = input()
   if heroi != "FIM":
       atributosL = input()
       atributos = atributosL.split(" - ")

       vidaHeroiL = atributos[0].split("vida ")
       agilHeroiL = atributos[1].split("agilidade ")
       armaHeroiL = atributos[2].split("arma ")

       vidaHeroi = vidaHeroiL[1]
       agilHeroi = agilHeroiL[1]
       armaHeroi = armaHeroiL[1]

       dicionario.update({heroi:{1:vidaHeroi, 2:agilHeroi, 3:armaHeroi}})

# condição
if len(dicionario) >= 3:
    print("Os portões do castelo se abrem e os heróis marcham rumo ao campo de batalha. O confronto contra o Rei Demônio começa agora!")
    vidaDem = 100
    agilDem = 32
    danoDem = 25

    # início da batalha
    parar = False
    heroisMortos = []
    while vidaDem > 0 and len(dicionario) > 0 and parar == False:
        heroi = input()
        herois = dicionario.keys()
        # heroi não vivo ou nao existe
        if heroi not in herois:
            print("Nenhum herói com esse nome está no campo de batalha. O Rei Demônio aguarda impacientemente por seu próximo adversário!")
        else:        
            dicionarioH = dicionario[heroi]
            agilHeroiA, vidaHeroiA, armaHeroiA = dicionarioH[2], dicionarioH[1], dicionarioH[3]
            agilHeroiA = int(agilHeroiA)
            vidaHeroiA = int(vidaHeroiA)
            primeiroAtaqueDoHeroi = False

            if vidaHeroiA > 0:
                # primeiro ataque - heroi
                if agilHeroiA > agilDem:
                    vidaDem -= calcularDanoHeroi(armaHeroiA, heroi)
                    primeiroAtaqueDoHeroi = True

                # primeiro ataque - demonio
                else:
                    primeiroAtaqueDoHeroi = False
                    print(f"O Rei Demônio avançou com suas garras infernais e atingiu {heroi}, causando 25 pontos de dano!")
                    vidaHeroiA -= danoDem

                # contra - ataque
                if vidaHeroiA > 0 and vidaDem > 0:
                    if primeiroAtaqueDoHeroi:
                        print(f"O Rei Demônio avançou com suas garras infernais e atingiu {heroi}, causando 25 pontos de dano!")
                        vidaHeroiA -= danoDem
                    else:
                        vidaDem -= calcularDanoHeroi(armaHeroiA, heroi)
                
                dicionario[heroi][1] = vidaHeroiA
                # validação de morte
                if vidaHeroiA <= 0:
                    print(f"{heroi} tombou diante do poder do Rei Demônio!")
                    heroisMortos.append(heroi)
                    del dicionario[heroi]

                # checagens finais
                if len(dicionario) == 0 and vidaDem > 0:
                    print("O último herói tombou. Vitorioso, o Rei Demônio retoma sua marcha sombria em direção ao Reino Celeste!")
                    parar = True
                if vidaDem <= 0:
                    print(f"Com um golpe decisivo, {heroi} derrota o Rei Demônio! Após uma longa batalha, o Reino Celeste está finalmente livre de sua ameaça!")
                    parar = True
                    if len(heroisMortos) == 0:
                        print("Contra todas as expectativas, todos os heróis retornaram vivos ao Reino Celeste. Naquela noite, nenhuma nova inscrição precisou ser feita no Memorial dos Heróis.")
                        parar = True
                    else:
                        print("A vitória foi conquistada, mas teve seu preço. Alguns heróis não retornaram do campo de batalha e seus nomes serão eternizados no Memorial dos Heróis.")
                        parar = True
            else:
                if heroi in dicionario.keys():
                    heroisMortos.append(heroi)
                    del dicionario[heroi]
            
    if len(heroisMortos) >=1:
        print("--- Memorial dos Heróis Caídos ---")
        for i in range(len(heroisMortos)):
            print(heroisMortos[i])

else:
   print("Poucos atenderam ao chamado do reino... Sem ao menos três heróis para formar a resistência, o Reino Celeste parece condenado à ruína!") 
