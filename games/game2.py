import random
from engine.game_engine import run_game

# Функция для генерации геометрической прогрессии
def generate_geometric_progression():
    # Генерация случайных параметров для прогрессии
    first_term = random.randint(1, 10)  # первый элемент прогрессии
    ratio = random.randint(2, 5)  # знаменатель прогрессии (обычно число больше 1)
    length = random.randint(5, 10)  # длина прогрессии (от 5 до 10)

    progression = [first_term * (ratio ** i) for i in range(length)]

    # Выбираем случайную позицию для пропущенного числа
    missing_index = random.randint(0, length - 1)
    missing_value = progression[missing_index]

    # Заменяем пропущенное число на две точки
    progression[missing_index] = '..'

    return progression, missing_value


# Функция для игры
def play_game():
    print("What number is missing in the progression?")

    # Генерация прогрессии
    progression, missing_value = generate_geometric_progression()

    # Выводим вопрос с пропущенным числом
    print("Question:", end=" ")
    for num in progression:
        print(num, end=" ")
    print()  # Для перехода на новую строку после вывода прогрессии

    # Получаем ответ пользователя
    user_answer = input("Your answer: ")

    # Проверяем ответ
    try:
        user_answer = int(user_answer)
        if user_answer == missing_value:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{missing_value}'.")
            print("Let's try again!")
    except ValueError:
        print("Invalid input! Please enter a number.")


# Запуск игры
if __name__ == "__main__":
    run_game(play_game)
