from package_hw8.module_hw8 import get_questions, get_statistics, get_final_values


def main():

    questions = get_questions()

    for i in range(len(questions)):
        print(questions[i].build_question())
        user_answer = input("Введите ответ!\n")
        # далее присвоение значения пользовательского ввода полю user_answer экземпляра класса Question
        # (ответ пользователя)
        questions[i].user_answer = user_answer
        # далее присвоение значения пользовательского ввода полю correctness_answer экземпляра класса Question
        # (True/False)
        questions[i].correctness_answer = questions[i].is_correct()
        if questions[i].is_correct():
            print(questions[i].build_positive_feedback())
        else:
            print(questions[i].build_negative_feedback())

    # Формирование статистики. Функция get_statistics() возвращает
    # список со значением правильности/неправильности (True/False) полученных ответов.
    list_correct_answers, list_points_received = get_statistics(questions)
    # Формирование данных из статистики. Функция get_final_values() возвращает
    # количество True ответов и суммарное количество баллов.
    number_correct_answers, number_points_received = get_final_values(list_correct_answers, list_points_received)

    print("\nВот и всё!\n"
          f"Отвечено верно на {number_correct_answers} вопрос из {len(questions)}\n"
          f"Набрано баллов: {number_points_received}")


main()
