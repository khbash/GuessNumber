import random

while True:
    secret_num = random.randint(1,50)
    attempts = 0

    while True:
        user_input = input("Введи свій варіант: ")

        if user_input.isdigit():
            guess = int(user_input)
            attempts += 1

            if guess < secret_num:
                print("Моє число більше")
            elif guess > secret_num:
                print("Моє число меньше")
            else:
                print("Вітаю! Ти вгадав число")
                break
        else:
            print("Помилка! тільки цифри")

    print("Чи хочете ви зіграти ще раз?")
    answer = input("Y/N: ").lower()
    if answer != "y":
        print("=" * 50)
        print("Дякую за гру! Повертайся ще")
        break

    print("=" * 50)
    print("Привіт знову!")
