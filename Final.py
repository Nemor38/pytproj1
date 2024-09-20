from kamennohnicibumaga import play_game
from faceNews import play_cuefa
from magicball import magic_ball
from orelorehka import orelorehka_game
from pomodo import calculate_percentage
import random
from random1o100 import randomaiser
from perimetr import perimetr_search
from random_pasword import random_password

true_log = 'dimasik'
true_pass = 'karasik'
user_log = input('Введи логин: ')
user_pass = input('Введи пароль: ')

# Проверка логина и пароля
while user_log != true_log or user_pass != true_pass:
    print('Неверный логин или пароль')
    user_log = input('Введи логин: ')
    user_pass = input('Введи пароль: ')
else:
    print('Вход выполнен')


# Функция помощника
def helper():
    print("Добро пожаловать, я ваш ЛИЧный помощник")

    options = [
        "1. Фейк-новости",
        "2. Игра 'Камень, Ножницы, Бумага'",
        "3. Магический шар",
        "4. Игра 'Орел & Решка'",
        "5. Найти периметр",
        "6. Калькулятор процентов",
        "7. Игра 'Угадай число'",
        "8. Создай 'Рандомный пароль'",
        "0. Выйти"
    ]

    while True:
        # Показ списка опций
        for option in options:
            print(option)

        # Запрос выбора
        choice = input("Введите номер выбранного раздела: ")

        # Обработка выбора
        if choice == "1":
            play_cuefa()  # Запуск игры "Фейк-новости"
        elif choice == "2":
            play_game()  # Игра "Камень, Ножницы, Бумага"
        elif choice == "3":
            magic_ball()  # Магический шар
        elif choice == "4":
            orelorehka_game()  # Игра "Орел & Решка"
        elif choice == "5":
            perimetr_search()  # Найти периметр
        elif choice == "6":
            calculate_percentage()  # Калькулятор процентов
        elif choice == "7":
            randomaiser()  # Игра "Угадай число"
        elif choice == "8":
            random_password()  # Создание рандомного пароля
        elif choice == "0":
            print("Выход из программы.")
            break  # Прерывание цикла и выход из программы
        else:
            print("Неверный выбор, попробуйте снова.")


helper()
