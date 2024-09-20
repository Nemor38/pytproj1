import random




def orelorehka_game():
    print("Добро пожаловать в игру орел&решка")
    options = ["Орел", "Решка"]

    while True:
        print("\nВыберите:")
        print("1 - Орел")
        print("2 - Решка")
        print("0 - Выход из игры")


        user_choice = int(input("Ваш выбор: "))

        if user_choice == 0:
            print("Спасибо за игру! До встречи.")
            break
        elif user_choice not in [1, 2]:
            print("Некорректный выбор. Пожалуйста, выберите число от 1 до 2.")
            continue

        user_option = options[user_choice - 1]
        computer_option = random.choice(options)
        print(f"Вы выбрали: {user_option}")
        print(f"Компьютер выбрал: {computer_option}")

        if user_option == computer_option:
            print("Ничья!")
        elif (user_option == "Орел" and computer_option == "Орел") or \
                (user_option == "Решка" and computer_option == "Решка"):
            print("Вы победили!")
        else:
            print("Вы проиграли!")


