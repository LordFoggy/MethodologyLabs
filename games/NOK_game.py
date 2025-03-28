import random

# Функция для вычисления НОД
def nod(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для вычисления НОК
def nok(a, b):
    return abs(a * b) // nod(a, b)

# Функция для генерации вопроса
def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    num3 = random.randint(1, 50)

    # Вычисление НОК для трех чисел
    result = nok(nok(num1, num2), num3)

    question = f"Question: {num1} {num2} {num3}"
    return question, result
    
