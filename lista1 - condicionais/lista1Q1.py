warriors = int(input())
print("Nossa, que lindo cavalo! Mas deixe-me verificar apenas uma coisa...")
if(warriors == 0):
    print("ENTRADA LIBERADA")
else:
    print("ARMADILHA")
    if(warriors % 2 == 0):
        duos = warriors//2
        print(f"OS GUERREIROS FORMARAM {duos} DUPLAS")
    else:
        duos = warriors//2
        print(f"OS GUERREIROS FORMARAM {duos} DUPLAS E UM GUERREIRO FICOU SOZINHO")