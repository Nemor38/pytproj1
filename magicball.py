import random


def magic_ball():
    answers = [
        "Бесспорно", "Предрешено", "Никаких сомнений",
        "Определённо да", "Можешь быть уверен в этом",
        "Мне кажется — «да»", "Вероятнее всего",
        "Хорошие перспективы", "Знаки говорят — «да»",
        "Да", "Пока не ясно, попробуй снова", "Спроси позже",
        "Лучше не рассказывать", "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять", "Даже не думай",
        "Мой ответ — «нет»", "По моим данным — «нет»",
        "Перспективы не очень хорошие", "Весьма сомнительно"
    ]

    print("Привет! Я магический шар, и я могу ответить на любой твой вопрос.")
    name = input("Как тебя зовут? ")
    print(f"Привет, {name}!")

    while True:
        question = input("Задай свой вопрос : ")
        print("Мой ответ:", random.choice(answers))
        print()



