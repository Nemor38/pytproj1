import random
import string
def random_password():
    def generate_password(length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    length = int(input("Введите длину пароля: "))
    print(f"Сгенерированный пароль: {generate_password(length)}")