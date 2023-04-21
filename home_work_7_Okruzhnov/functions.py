import json


def load_students():
    """
    Загружает список студентов из файла students.json в формате JSON,
    распаковывает из JSON и преобразует в объект Python.
    Возвращает list со вложенными dict.
    """
    with open("students.json", "r", encoding="utf-8") as file:
        students_list = json.load(file)
        return students_list


def load_professions():
    """
    Загружает список профессий из файла professions.json в формате JSON,
    распаковывает из JSON и преобразует в объект Python.
    Возвращает list со вложенными dict.
    """
    with open("professions.json", "r", encoding="utf-8") as file:
        professions_list = json.load(file)
        return professions_list


def get_student_by_pk(pk):
    """
    Принимает значение порядкового номера студента и достает из списка студентов,
    вызвав функцию load_students(), вложенный словарь с атрибутами соответствующего студента.
    """
    pk = int(pk)
    students_list = load_students()
    for i in students_list:
        if pk == i['pk']:
            return students_list[i['pk'] - 1]
    else:
        print("У нас нет такого студента")
        quit()


def get_profession_by_title(title):
    """
    Принимает значение наименования профессии и достает из списка профессий,
    вызвав функцию load_professions(), вложенный словарь с атрибутами соответствующей профессии.
    """
    professions_list = load_professions()
    for i in professions_list:
        if title == i['title']:
            return professions_list[i['pk'] - 1]
    else:
        print("У нас нет такой специальности")
        quit()


def check_fitness(student, profession):
    """
    Принимает значения порядкового номера студента и наименования профессии от пользовательского ввода
    из глобальной области.
    Путем преобразования в множество и сравнения этих множеств определяет навыки в наличии и недостающие навыки.
    В зависимости от результатов сопоставления определяет степени пригодности.
    Указанные три значения возвращаются в словаре student_fitness.
    """
    student_fitness = {}

    unique_student_skills = set(get_student_by_pk(student).get('skills'))
    required_professional_skills = set(get_profession_by_title(profession).get('skills'))

    has_set = required_professional_skills.intersection(unique_student_skills)
    lacks_set = required_professional_skills.difference(unique_student_skills)

    has_list = list(has_set)
    lacks_list = list(lacks_set)

    fit_percent = None  # Переменная, принимающая значение степени пригодности.

    if len(lacks_list) == len(required_professional_skills):
        fit_percent = 0
    elif len(has_list) >= len(required_professional_skills):
        fit_percent = 100
    else:
        fit_percent = int(round((100 - (100 * len(has_set) / len(lacks_set))), -1))

    student_fitness["has"] = has_list
    student_fitness["lacks"] = lacks_list
    student_fitness["fit_percent"] = fit_percent

    return student_fitness
