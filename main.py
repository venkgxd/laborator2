from random import randint
N = randint(1,10)
attempc = 3
while attempc > 0:
    user_number = int(input("Введите число от 1 до 10:"))
    if N == user_number:
        print("Вы угадали!")
    else:
        print("Не угадал(")
        attempc -= 1