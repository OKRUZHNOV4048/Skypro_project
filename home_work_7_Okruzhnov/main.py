from functions import get_student_by_pk, get_profession_by_title, check_fitness


def main():

    student = input("Введите номер студента\n")
    if student.isdigit() is True:
        student_info = get_student_by_pk(student)
    else:
        print('У нас нет такого студента')
        quit()

    print(f"Студент {student_info['full_name']}")
    print(f"Студент знает {', '.join(student_info['skills'])}")

    title = input(f"Выберите специальность для оценки студента {student_info['full_name']}\n")
    title = title.title()
    profession_info = get_profession_by_title(title)

    profession_info = check_fitness(student, title)
    print(profession_info)
    print(f"Пригодность {profession_info['fit_percent']}%")
    print(f"{student_info['full_name']} знает {', '.join(student_info['skills'])}")
    print(f"{student_info['full_name']} из того, что нужно знает {', '.join(profession_info['has'])}")
    print(f"{student_info['full_name']} не знает {', '.join(profession_info['lacks'])}")


main()
