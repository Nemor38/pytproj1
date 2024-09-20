import random

def randomaiser():
    print('Привет это игра угадай число 1 до 100, начнем?')
    truecheslo = random.randint(1, 100)

    while True:
        user_choise = int(input('твой выбор:'))
        if truecheslo > user_choise:
            print('попробуй большее число')
        elif truecheslo < user_choise:
            print('попробуй меньшее число')
        else:
            print('Молодец! Ты выиграл!')
            break

