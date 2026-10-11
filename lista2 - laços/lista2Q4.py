print("Tigresa: Duvido você bater o recorde, Po!")
print("Po: Prepare-se para ver o Dragão Guerreiro em ação!")
rodadas = int(input())
recorde = int(input())
total = 0
i = 0
ganhouComUmaRodada = False

while i < rodadas and not ganhouComUmaRodada:
    bandejas = int(input())
    totalRodada = 0
    b = 0
    while b < bandejas and not ganhouComUmaRodada:
        bolinhos = int(input())
        totalRodada += bolinhos
        if totalRodada > recorde:
            ganhouComUmaRodada = True
        b += 1
    total += totalRodada
    if not ganhouComUmaRodada:
        if totalRodada >= 10:
            print("\nPo: Delícia! Mais uma rodada finalizada!")
        else:
            print("\nPo: Ainda tenho espaço para mais!")
        print(f"Rodada {i+1}: Po comeu {totalRodada} bolinhos.")
    i += 1

if ganhouComUmaRodada:
    print("\nTigresa: Mas como?!")
    print("Po: UHUL! CONHEÇA A FORÇA DO DRAGÂO GUERREIRO!!")
    print(f"Rodada {i}: Po comeu {totalRodada} bolinhos.")
    print("\nPo: Ei! Eu ainda não terminei!")
    print("Tigresa: Acho que não vou mais subestimar sua fome.")
    print(f"Que loucura! Po venceu a aposta comendo um total de {totalRodada} bolinhos em uma só rodada!")
elif total > recorde:
    print(f"\nPo: Eu sabia que conseguiria! O recorde e meu!")
    print(f"Tigresa: Inacreditável... Você realmente venceu a aposta.")
    print(f"Po venceu a aposta! Ele comeu um total de {total} bolinhos e superou o recorde de {recorde}!")
elif total == recorde:
    print(f"\nPo: Empatamos! Cheguei exatamente no recorde!")
    print(f"Tigresa: Impressionante, mas empatar não basta para vencer a aposta. Venha lavar a louça!")
    print(f"Houve um empate! Po comeu exatamente {total} bolinhos e igualou o recorde de {recorde}.")
else:
    print(f"\nTigresa: Eu avisei, Po! A louça do palácio te espera.")
    print(f"Po: Ah não... Minhas mãos vão ficar enrugadas...")
    print(f"Tigresa venceu a aposta! Po comeu apenas {total} bolinhos e não alcançou o recorde de {recorde}.")