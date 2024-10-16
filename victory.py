# знаменитости и их годы рождения
celebrities = {
    "А.С. Пушкин": 1799,#правильный ответ 1799
    "Лев Толстой": 1828,#правильный ответ 1828
    "Федор Достоевский": 1821,#правильный ответ 1821
    "Владимир Путин": 1952,#правильный ответ 1952
    "Михаил Ломоносов": 1711#правильный ответ 1711
}

while True:
    correct_answers = 0  # счётчик правильных ответов
    mistakes = 0  # счётчик ошибок
    total_questions = len(celebrities)  # количество вопросов

    # проходим по каждой знаменитости
    for celebrity in celebrities:
        user_input = int(input(f"Введите год рождения {celebrity}: "))
        if user_input == celebrities[celebrity]:
            print("Верно!")
            correct_answers += 1  # увеличиваем счётчик на 1, если ответ верный
        else:
            print(f"Неверно! Правильный ответ: {celebrities[celebrity]}")
            mistakes += 1  # увеличиваем счётчик ошибок

    # вычисляем процент правильных и неправильных ответов
    correct_answers_percent = (correct_answers * 100) / total_questions
    mistakes_percent = (mistakes * 100) / total_questions

    # выводим результаты
    print("\nКоличество правильных ответов:", correct_answers)
    print("Количество неправильных ответов:", mistakes)
    print("Процент правильных ответов:", correct_answers_percent)
    print("Процент неправильных ответов:", mistakes_percent)

    # спрашиваем пользователя, хочет ли он начать игру сначала
    retry = input("Хотите начать игру сначала? да/нет: ")
    if retry != "да":
        print("Спасибо за игру!")
        break




