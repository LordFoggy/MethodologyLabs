import random

# Функция для генерации геометрической прогрессии
def generate_geometric_progression():
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

# Функция для генерации вопроса
def generate_question():
    progression, missing_value = generate_geometric_progression()

    question = "Question: " + " ".join(map(str, progression))
    return question, missing_value
    
