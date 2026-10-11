print("Quando percebi que contara oito mortes, senti o peso da minha própria lenda")
qnt_ataques = int(input())

i = 0
x = 0
n = 0

item = ""
companheiro = ""
frases = ""
frase_gato = ""
divisiveis3 = 0
chegouDesfecho = False

if qnt_ataques > 0:
    while qnt_ataques > 0 and not chegouDesfecho:
        print("Preciso encontrar esse mapa a qualquer custo, nem que seja a última coisa que eu faça com esta vida!")
        companheiro  = str(input())

        if "cao perrito" in companheiro.lower():
            print("Olha só... de todas as criaturas do mundo, justo você tinha que decidir me seguir com esse rabo abanando?")
            n = int(input())
            x=0
            divisiveis3 = 0
            for x in range(n):
                numero = int(input())
                if numero % 3 == 0:
                    divisiveis3 += 1
            if divisiveis3 == n:
                print("Bom trabalho, meu garoto! Quem diria que um cãozinho tão pequeno seria o grande herói do dia?")
                chegouDesfecho = True
        elif "kitty patamansa" in companheiro.lower() and not chegouDesfecho:
            print("Kitty... Olhar para você de novo só me faz lembrar que, entre todas as minhas nove vidas, o meu maior erro foi ter deixado você esperando.")
            item = str(input())
            if "chapeu do gato" in item.lower() or "bota do gato" in item.lower():
                print("Impressionante, Kitty... Sempre soube que você era rápida, mas admito que nada fica melhor nas mãos da melhor ladra de Tão Tão Distante do que um presente para mim.")
                chegouDesfecho = True
        else:
            frases = ""
            while "morte" not in frases.lower() and "desfecho" not in frases.lower() and not chegouDesfecho:
                frases = str(input())
                if "desfecho" in frases.lower():
                    chegouDesfecho = True
        if chegouDesfecho:
            chegouDesfecho = True

        qnt_ataques -= 1
   
else:
    print("Até logo, velho amigo... É bom saber que finalmente posso respirar fundo e apenas viver o dia de hoje.")

if chegouDesfecho:
    print("Parece que essa família de ursos e sua cachinhos acabam de provar do verdadeiro felino de botas!")
    frase_gato = str(input())
    if "coragem" in frase_gato.lower():
        print("A verdadeira vitória não está em vencer a morte, mas em encará-la de frente e escolher lutar por cada segundo desta vida!")
    else:
        print("Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje a lenda finalmente descansa.")
else:
    print("Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje a lenda finalmente descansa.")