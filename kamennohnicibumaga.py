import random

def play_game():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    options = ["Камень", "Ножницы", "Бумага"]

    while True:
        print("\nВыберите:")
        print("1 - Камень")
        print("2 - Ножницы")
        print("3 - Бумага")
        print("0 - Выход из игры")

        try:
            user_choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Пожалуйста, введите число от 0 до 3.")
            continue

        if user_choice == 0:
            print("Спасибо за игру! До встречи.")
            break
        elif user_choice not in [1, 2, 3]:
            print("Некорректный выбор. Пожалуйста, выберите число от 1 до 3.")
            continue

        user_option = options[user_choice - 1]
        computer_option = random.choice(options)
        print(f"Вы выбрали: {user_option}")
        print(f"Компьютер выбрал: {computer_option}")

        if user_option == computer_option:
            print("Ничья!")
        elif (user_option == "Камень" and computer_option == "Ножницы") or \
             (user_option == "Ножницы" and computer_option == "Бумага") or \
             (user_option == "Бумага" and computer_option == "Камень"):
            print("Вы победили!")
        else:
            print("Вы проиграли!")


