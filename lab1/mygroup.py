# Входные данные
students = [
    {
        "name": "Зывль",
        "surname": "Cкотский",
        "exams": ["Жежь", "Пепь", "Вепь"],
        "marks": [1, 3, 2]
    },
    {
        "name": "Цулийманя",
        "surname": "Ыъъыя",
        "exams": ["ГиБ", "АиГ", "БиВ"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "Винишко", "Пасош"],
        "marks": [5, 6, 7]
    }
]

# Задание
# Необходимо написать функцию фильтрации студентов по средней оценке,
# так, чтобы на экран выводился список студентов, средний балл которых выше заданного.
# Средний балл, по которому будет проводиться фильтрация, вводится
# пользователем с клавиатуры

def avg_student_score(student):
    _marks = student["marks"]
    return int(sum(_marks) / len(_marks))

def print_studs(avg_score_filter):
    for student in students:
        avg_score_current = avg_student_score(student)
        if avg_score_current >= avg_score_filter:
            print(u"Имя".ljust(15),
                  u"Фамилия".ljust(10),
                  u"Средняя оценка".ljust(20))
            print(student["name"].ljust(15),
                  student["surname"].ljust(10),
                  avg_score_current
                  )

def main():
    while True:
        try:
            avg_score_filter = int(input("Средняя оценка для сортировки: "))
            print_studs(avg_score_filter)
        except ValueError:
            print("Это не цифра, выходю.")
            break

if __name__=="__main__":
    main()
