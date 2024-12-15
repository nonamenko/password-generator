import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Генератор паролів ===")
    try:
        length = int(input("Введіть довжину пароля (мінімум 8): "))
        if length < 8:
            print("Довжина пароля має бути не менше 8 символів.")
            return
        password = generate_password(length)
        print(f"Ваш пароль: {password}")
    except ValueError:
        print("Будь ласка, введіть число.")

if __name__ == "__main__":
    main()
