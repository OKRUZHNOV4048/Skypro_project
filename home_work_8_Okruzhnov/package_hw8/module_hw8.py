import json
import random


class Question:
    def __init__(self, question_text, question_complex, correct_answer, user_answer=None, correctness_answer=False):
        self.question_text = question_text
        self.question_complex = question_complex
        self.correct_answer = correct_answer
        self.user_answer = user_answer
        self.correctness_answer = correctness_answer

    def __str__(self):
        return f"""
               Вопрос: {self.question_text},
               Сложность: {self.question_complex};
               Правильный ответ: {self.correct_answer};
               Ответ пользователя: {self.user_answer};
               Правильность ответа: {self.correctness_answer}.
               """

    def get_points(self):
        """
        Возвращает количество балов в зависимости от сложности.
        """
        return int(self.question_complex) * 10

    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает с верным ответом, иначе False.
        """
        if self.user_answer == self.correct_answer:
            return True
        return False

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде.
        """
        return f"{self.question_text}\nСложность: {self.question_complex}"

    def build_positive_feedback(self):
        """
        Возвращает:
        Ответ верный, получено __ баллов
        """
        return f"Ответ верный, получено {self.get_points()} баллов"

    def build_negative_feedback(self):
        """
        Возвращает:
        Ответ неверный, верный ответ __
        """
        return f"Ответ неверный. Верный ответ – {self.correct_answer}"


def load_questions():
    """
    Загружает список вопросов с атрибутами вопросов из файла questions.json в формате JSON,
    распаковывает из JSON и преобразует в объект Python.
    Возвращает list со вложенными dict.
    """
    with open("questions.json", "r", encoding="utf-8") as file:
        questions_data_list = json.load(file)
        return questions_data_list


def get_questions():
    """
    Создает и возвращает список questions с экземплярами класса Question.
    """
    questions_data_list = load_questions()
    questions = []
    for i in range(len(questions_data_list)):
        question = Question(questions_data_list[i]["question_text"], questions_data_list[i]["question_complex"],
                            questions_data_list[i]["correct_answer"])
        questions.append(question)
    random.shuffle(questions)
    return questions


def get_statistics(questions):
    """
    Формирование статистики. Функция get_statistics() возвращает
    список со значением правильности/неправильности (True/False) полученных ответов.
    """
    list_correct_answers = []
    list_points_received = []
    for i in range(len(questions)):
        list_correct_answers.append(questions[i].correctness_answer)
        if questions[i].correctness_answer:
            list_points_received.append(questions[i].get_points())
        else:
            list_points_received.append(0)
    return list_correct_answers, list_points_received


def get_final_values(list_correct_answers, list_points_received):
    """
    Формирование данных из статистики. Функция get_final_values() возвращает
    количество True ответов и суммарное количество баллов.
    """
    return list_correct_answers.count(True), sum(list_points_received)
