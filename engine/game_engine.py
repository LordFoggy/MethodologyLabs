def run_game(generate_question_fn):
    rounds = 3
    for _ in range(rounds):
        question, correct_answer = generate_question_fn()

        # Выводим вопрос
        print(question)

        # Получаем ответ от пользователя
        user_answer = input("Your answer: ")

        # Проверка ответа
        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                print("Correct!")
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print("Let's try again!")
        except ValueError:
            print("Invalid input! Please enter a number.")
            
