perigo=100
zerou=False
ajuda = ""
recruta = ""
i = 0

print("Os pinguins começaram sua fuga. Operação: sair de Mônaco vivos!")
rodadas = int(input())

for i in range(rodadas):
    if perigo > 0:
        acao = str(input())
        if "CHANTEL DUBOUIS" in acao.upper():
            print("Parece que a Capitã Dubouis ganhou uma ajudinha extra na caçada... Como se ela precisasse.")
            ajuda = str(input())
            if "helicóptero" in ajuda.lower():
                print("Pendurada em um helicóptero, Dubouis se aproxima cada vez mais dos fugitivos!")
                perigo += 15
            elif "rastrear" in ajuda.lower():
                print("Dubouis encontrou os rastros dos animais. Infelizmente, despistar essa mulher não estava no plano.")
                perigo += 20
            elif "SCOOTER" in ajuda.upper():
                print("ELA PEGOU A LENDÁRIA SCOOTER! OS PINGUINS REALMENTE TÊM ALGUMA CHANCE?!")
                perigo += 35
            elif "non, je ne regrette rien" in ajuda.lower():
                print("INACREDITÁVEL! A VOZ ANGELICAL DE DUBOIS REANIMOU TODA A EQUIPE! ISSO É PERMITIDO?!")
                perigo += 100
            else:
                print("Um dos capangas encontrou uma pista dos animais. Pequena pista, enorme problema.")
                perigo += 5
        elif "kowalski" in acao.lower():
            print("Kowalski teve uma ideia! Por algum milagre, ela realmente funcionou e atrasou a caçadora.")
            perigo -= 30
        elif "capitão" in acao.lower():
            print("Após uma troca de golpes com Dubouis, o Capitão conseguiu atrasá-la. Liderança também envolve pancadaria.")
            perigo -= 40
        elif "RICO" in acao.upper():
            print("Rico sacou uma bomba de procedência extremamente duvidosa e acertou em cheio! Clássico Rico.")
            perigo -= 50
        else:
            print("Parece que o Recruta vai tentar ajudar na fuga... Que os céus protejam essa operação.")
            recruta = str(input())
            if "sucesso" in recruta.lower():
                print("ELE CONSEGUIU! A fofura do Recruta distraiu os guardas de Dubouis. Uma arma verdadeiramente devastadora.")
                perigo -= 15
            else:
                print("Ele tentou... mas deixou um rastro enorme para os guardas. Pelo menos a intenção foi boa.")
                perigo += 10  
        if perigo <= 0:
            zerou = True      
    else:
        zerou=True

if zerou:
    print("ELES CONSEGUIRAM! Deixaram a grandiosa CHANTEL DUBOUIS para trás e seguiram rumo a Madagascar!")
else:
    print("Os pinguins não tiveram chance... A maior caçadora de animais de Mônaco é simplesmente IMPLACÁVEL!")