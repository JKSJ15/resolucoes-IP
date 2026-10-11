print("=== WABAC: SISTEMA DE EMERGÊNCIA ===")
print("Alvo: Ano 2026 | Peças Necessárias: 3")
print("Sherman, mantenha as mãos longe dos botões! Iniciando saltos...")

ano_origem = int(input())
ano_proibido = int(input())
energia = int(input())
ano_atual = ano_origem
rasgo_temporal = 0
pecas = 0
parar = False
saltos = 0

while not parar:
    acao = str(input())
    if "SALTAR" in acao.upper() and not parar:
        anos_salto = int(input())
        custo_energia = int(input())
        ano_atual += anos_salto
        energia -= custo_energia
        rasgo_temporal += 10
        saltos += 1
        energia = max(energia, 0)
        rasgo_temporal = min(rasgo_temporal, 100)
        
        if (saltos > 1 and ano_atual == ano_origem) or ano_atual == ano_proibido:
            print(f"ALERTA CRÍTICO: Peabody encontrou sua própria versão no ano {ano_atual}!")
            print("O continuum espaço-tempo ruiu em uma espiral paradoxal.")
            parar = True
        elif energia <= 0:
            print("A WABAC desligou completamente por falta de energia.")
            print("Peabody e Sherman estão vagando sem rumo pela linha do tempo...")
            parar = True
        elif rasgo_temporal >= 100:
            print("O rasgo temporal atingiu massa crítica!")
            print("O universo foi engolido por um buraco negro sobre a cidade de Nova York.")
            parar = True
        elif pecas >= 3 and ano_atual >= 2026:
            print(f'A WABAC emergiu com sucesso no ano de {ano_atual}! Com as 3 peças coletadas, Mr. Peabody selou o rasgo temporal e salvou o presente!')
            parar = True
        else:
            print(f"WABAC saltou para o ano {ano_atual}!")
            print(f"Energia restante: {energia} | Rasgo Temporal: {rasgo_temporal}%")

    elif "CONSERTAR" in acao.upper() and not parar:
        dificuldade = int(input())
        esforco_sherman = int(input())
        if esforco_sherman >= dificuldade:
            pecas += 1
            energia -= 10
            energia = max(energia, 0)
            if energia <= 0:
                print("A WABAC desligou completamente por falta de energia.")
                print("Peabody e Sherman estão vagando sem rumo pela linha do tempo...")
                parar = True
            elif rasgo_temporal >= 100:
                print("O rasgo temporal atingiu massa crítica!")
                print("O universo foi engolido por um buraco negro sobre a cidade de Nova York.")
                parar = True
            elif pecas >= 3 and ano_atual >= 2026:
                print(f'A WABAC emergiu com sucesso no ano de {ano_atual}! Com as 3 peças coletadas, Mr. Peabody selou o rasgo temporal e salvou o presente!')
                parar = True
            else:
                print('Sherman: "Consegui, Mr. Peabody! Encontrei uma peça de calibragem!"')
                print(f"Peças coletadas: {pecas}/3 | Energia: {energia}")
        else:
            if not parar:
                
                energia -= 15
                rasgo_temporal += 20
                energia = max(energia, 0)
                rasgo_temporal = min(rasgo_temporal, 100)
                if energia <= 0:
                    print("A WABAC desligou completamente por falta de energia.")
                    print("Peabody e Sherman estão vagando sem rumo pela linha do tempo...")
                    parar = True
                elif rasgo_temporal >= 100:
                    print("O rasgo temporal atingiu massa crítica!")
                    print("O universo foi engolido por um buraco negro sobre a cidade de Nova York.")
                    parar = True
                else:
                    print('Mr. Peabody: "Tenha mais cuidado, Sherman! Essa falha desestabilizou o tempo!"')
                    print(f"Energia: {energia} | Rasgo Temporal: {rasgo_temporal}%")
    elif  "AULA DE HISTÓRIA" in acao.upper():
        print('Mr. Peabody: "Como disse Galileu Galilei, a matemática é a linguagem com a qual Deus escreveu o universo."')
        energia += 25
        rasgo_temporal += 15
        rasgo_temporal = min(rasgo_temporal, 100)
        if energia <= 0:
            print("A WABAC desligou completamente por falta de energia.")
            print("Peabody e Sherman estão vagando sem rumo pela linha do tempo...")
            parar = True
        elif rasgo_temporal >= 100:
            print("O rasgo temporal atingiu massa crítica!")
            print("O universo foi engolido por um buraco negro sobre a cidade de Nova York.")
            parar = True
        elif pecas >= 3 and ano_atual >= 2026:
            print(f'A WABAC emergiu com sucesso no ano de {ano_atual}! Com as 3 peças coletadas, Mr. Peabody selou o rasgo temporal e salvou o presente!')
            parar = True
        else:
            print(f"Energia recarregada para {energia}!")

    elif "ABORTAR" in acao.upper():
        parar = True
        print("Mr. Peabody acionou o protocolo de parada manual.") 
        print("A viagem foi cancelada antes de sua conclusão.")