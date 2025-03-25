import random
from engine.game_engine import run_game

# Функция для вычисления НОД
def nod(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для вычисления НОК
def nok(a, b):
    return abs(a * b) // nod(a, b)

# Функция для генерации случайных чисел и игры
def play_game():
    print("Find the smallest common multiple of given numbers.")

    # Генерация случайных чисел
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    num3 = random.randint(1, 50)

    # Вычисление НОК для трех чисел
    result = nok(nok(num1, num2), num3)

    # Вывод вопроса и получение ответа пользователя
    print(f"Question: {num1} {num2} {num3}")
    user_answer = input("Your answer: ")

    # Проверка ответа
    try:
        user_answer = int(user_answer)
        if user_answer == result:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print("Let's try again!")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Запуск игры
if __name__ == "__main__":
    run_game(play_game)
