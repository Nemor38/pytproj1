def calculate_percentage():
    print("Простой калькулятор процентов")
    print("Выберите операцию:")
    print("1. Найти процент от числа")
    print("2. Узнать, сколько процентов одно число составляет от другого")
    print("3. Увеличить число на процент")
    print("4. Уменьшить число на процент")
    print("Введите 'exit' для выхода")

    while True:
        choice = input("Введите номер операции: ")

        if choice.lower() == 'exit':
            print("Выход из программы.")
            break

        if choice == '1':
            number = float(input("Введите число: "))
            percent = float(input("Введите процент: "))
            result = (number * percent) / 100
            print(f"{percent}% от {number} = {result}")

        elif choice == '2':
            part = float(input("Введите часть: "))
            whole = float(input("Введите целое: "))
            result = (part / whole) * 100
            print(f"{part} составляет {result}% от {whole}")

        elif choice == '3':
            number = float(input("Введите число: "))
            percent = float(input("Введите процент: "))
            result = number + (number * percent) / 100
            print(f"{number} увеличено на {percent}% = {result}")

        elif choice == '4':
            number = float(input("Введите число: "))
            percent = float(input("Введите процент: "))
            result = number - (number * percent) / 100
            print(f"{number} уменьшено на {percent}% = {result}")

        else:
            print("Некорректный выбор. Пожалуйста, выберите операцию от 1 до 4 или 'exit'.")



