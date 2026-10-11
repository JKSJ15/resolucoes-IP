print("Sistema HeisenbergOS v2.0 - Monitor do Reator Inicializado... \n")

reagentes_base = ("Metilamina", "Fenilacetona", "Hidróxido de Sódio", "Ácido Clorídrico", "Metilamina")
quantidades_ml = (500, 250, 150, 100, 300)
tupla = tuple(zip(reagentes_base, quantidades_ml))

print(tupla)

acao = ""
encerrar = False
cont = 0
index = 0
r1 = ""
r2 = ""
r3 = ""
m1 = ""
m2 = ""
m3 = ""

operador = input()
if "Hank Schrader" in operador or "Gomez" in operador:
    print("Alerta Vermelho: Agente do DEA detectado no laboratório!")
    
pressao_tanque = input()
if not pressao_tanque.isnumeric():
    print("Yo Jesse! Você colocou tempero onde devia ter um número de pressão! O reator pifou!")
    encerrar = True
else:
    status_mike = input() # "tranquilo" or "alerta"
    if status_mike == status_mike.upper():
        print("Abaixe o tom de voz! Mike está escutando no microfone!")

    while not "FIM" in acao and encerrar == False:
        acao = str(input()) #"contar", "posicao", "varrer", "concatenar", "desempacotar" ou "FIM"
        if not "FIM" in acao:
            if "contar" in acao or "posicao" in acao or "varrer" in acao:
                ingrediente_alvo = str(input())
                quantidade = reagentes_base.count(ingrediente_alvo)
                if "contar" in acao:
                    if ingrediente_alvo in reagentes_base:
                        print(f"O ingrediente {ingrediente_alvo} aparece {quantidade} vez(es) na receita base.")
                    else:
                        print(f"O Ingrediente {ingrediente_alvo} não foi encontrado, precisamos melhorar o nosso estoque!")
                elif "posicao" in acao:
                    if ingrediente_alvo in reagentes_base:
                        posicao = reagentes_base.index(ingrediente_alvo)
                        print(f"O ingrediente {ingrediente_alvo} foi encontrado primeiro na posicao {posicao} da tupla.")
                    else:
                        print(f"Ingrediente {ingrediente_alvo} nao encontrado no registro fixo!")
                elif "varrer" in acao:
                    cont = 0
                    for i in reagentes_base:
                        if i == ingrediente_alvo:
                            cont += 1
                    print(f"ingrediente {ingrediente_alvo} aparece {cont} vezes")
            elif "concatenar" in acao:
                novo_elemento = str(input())
                nova_quantidade = int(input())
                reagentes_base = reagentes_base + (novo_elemento,)
                quantidades_ml = quantidades_ml + (nova_quantidade,)
                tupla = tuple(zip(reagentes_base, quantidades_ml))
                tamanho = len(tupla)
                print(f"Ingrediente adicionado à nova tupla! Tamanho atualizado: {tamanho}")
            elif "desempacotar" in acao:
                r1 = reagentes_base[len(reagentes_base-1)]
                r2 = reagentes_base[len(reagentes_base-2)]
                r3 = reagentes_base[len(reagentes_base-3)]
                m1 = quantidades_ml[len(quantidades_ml-1)]
                m2 = quantidades_ml[len(quantidades_ml-2)]
                m3 = quantidades_ml[len(quantidades_ml-3)]
                print(f"Últimos 3 reativos do registro: {r1} ({m1}ml), {r2} ({m2}ml) e {r3} ({m3}ml).")