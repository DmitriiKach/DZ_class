class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = [] # изучаемые на данный момент курсы
        self.student_list.append(self)  # Добавим в список студентов вновь созданный экземпляр
        self.grades_student = {} # словарь с оценками студентов от проверяющих
        self.average_grade = 0 # Средняя оценка за ДЗ

        # Метод выставления оценок студентами лекторам
    def grades_for_lecturer(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grades]
            else:
                lecturer.grades_lecturer[course] = [grades]
        else:
            return 'Ошибка'

        # Метод для добавления пройденных курсов
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

        # Метод вычисления средней оценки за ДЗ :
    def average_grade_student(self):
        grade_list = []
        for val in self.grades_student.values():
            grade_list.extend(val)
            # Подсчитаем сумму оценок:
        sum_ = sum(grade_list)
            # Подсчитаем среднее значение всех оценок
        self.average_grade = round(sum_ / len(grade_list), 2)
        return self.average_grade

        # метод __str__ для Student :
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за ДЗ: {self.average_grade_student()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

        #  Метод сравнения средних оценок студентов:
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade < other.average_grade

class Mentor:
    mentor_list = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] # Подключенные курсы
        self.courses_in_progress = []
        self.grades_lecturer = {} # словарь с оценками лекторам от студентов
        self.average_grade = 0  # Средняя оценка за лекции
        self.mentor_list.append(self) # Добавление в список преподователей вновь созданного экземпляра


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecturer = {}

    # Метод вычисления средней оценки за лекции :
    def average_grade_lectures(self):
        grade_list = []
        for val in self.grades_lecturer.values():
            grade_list.extend(val)
        # Подсчитаем сумму оценок:
        sum_ = sum(grade_list)
        # Подсчитаем среднее значение всех оценок
        self.average_grade = round(sum_ / len(grade_list), 2)
        return self.average_grade

        #  Метод сравнения средних оценок лекторов:
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade
        
        # метод __str__ для Lecturer :
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за лекции: {self.average_grade_lectures()}'
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        # Метод, который позволяет проверяющему добавить оценку в словарь студента по названию курса:
    def rate_hw(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grades]
            else:
                student.grades_student[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f' Имя: {self.name} \n Фамилия: {self.surname}'
        return res

# Инициализация лекторов :
lecturer_1 = Lecturer('Misha','White')
lecturer_1.courses_attached.append('Python')
lecturer_2 = Lecturer('Anna','Dipl')
lecturer_2.courses_attached.append('Python')
# Инициализация студентов :
student_1 = Student('Vasya','Nogh','Male')
student_1.courses_in_progress.append('Python')
student_2 = Student('Maria','Rich','Female')
student_2.courses_in_progress.append('Python')
student_3 = Student('Elena','Gray','Female')
student_3.courses_in_progress.append('Python')
student_4 = Student('Ruoy', 'Eman', 'your_gender')
student_4.courses_in_progress += ['Python', 'Java']

# Выставим оценки лекторам
student_1.grades_for_lecturer(lecturer_1, 'Python', 9)
student_2.grades_for_lecturer(lecturer_1, 'Python', 9)
student_3.grades_for_lecturer(lecturer_1, 'Python', 7)
student_4.grades_for_lecturer(lecturer_1, 'Python', 8)

student_1.grades_for_lecturer(lecturer_2, 'Python', 9)
student_2.grades_for_lecturer(lecturer_2, 'Python', 8)
student_3.grades_for_lecturer(lecturer_2, 'Python', 5)
student_4.grades_for_lecturer(lecturer_2, 'Python', 8)

# Посмотрим оценки обоих лекторов(проверка):
print(lecturer_1.grades_lecturer)
print(lecturer_2.grades_lecturer)
# Вызов метода вычисления средней оценки лекторов
print(lecturer_1.average_grade_lectures())
print(lecturer_2.average_grade_lectures())
print(lecturer_1)
print(lecturer_2)

# Инициализируем проверяющих
reviewer_1 = Reviewer ('Petr','Maksimov')
reviewer_1.courses_attached.append('Python')
reviewer_2 = Reviewer('Some', 'Buddy')
reviewer_2.courses_attached += ['Python'] # Добавили курс 'Python' в список проверяемых курсов
# Зададим выставление оценок проверяющими (reviewer) студентам соответствующих курсов
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 6)
print(f'Оценки для {student_1.name} - {student_1.grades_student }')
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Python', 6)
print(f'Оценки для {student_2.name} - {student_2.grades_student }')
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 10)
print(f'Оценки для {student_3.name} - {student_3.grades_student }')
reviewer_2.rate_hw(student_4, 'Python', 10)
reviewer_2.rate_hw(student_4, 'Python', 10)
reviewer_2.rate_hw(student_4, 'Python', 10)
print(f'Оценки для {student_4.name} - {student_4.grades_student }')

# Проверка - Средняя оценка для студентов:
print(student_1.average_grade_student())
print(student_2.average_grade_student())
print(student_3.average_grade_student())
print(student_4.average_grade_student())

# Добавим курс в список текущих курсов
student_1.courses_in_progress.append('Git')
print(student_1.courses_in_progress)

# Добавим курс в список оконченных курсов :
student_1.finished_courses.append('Java')
# Проверка переопределения метода __str__ для студентов:
print(student_1)
print(student_2)
print(student_3)
print(student_4)

# 2) Реализуйте возможность сравнивать (через операторы сравнения)
# между собой лекторов по средней оценке за лекции и студентов по
# средней оценке за домашние задания.

# Проверим словари с оценками у лекторов:
print (lecturer_1.grades_lecturer)
print (lecturer_2.grades_lecturer)

# Средние оценки лекторов 1 и 2 :
lecturer_1.average_grade = lecturer_1.average_grade_lectures()
lecturer_2.average_grade = lecturer_2.average_grade_lectures()
print(lecturer_1.average_grade,lecturer_2.average_grade)
# Производим сравнение лекторов по средним оценкам за лекции
print(lecturer_1 < lecturer_2)

# Средние оценки студентов 1 и 2 :
student_1.average_grade = student_1.average_grade_student()
student_2.average_grade = student_2.average_grade_student()
print(student_1.average_grade,student_2.average_grade)

# Сравним студентов по средней оценке по ДЗ :
print(student_1 > student_2)

#
# print(student_list())
#  Функция для подсчета средней оценки за домашние задания по всем
#  студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса)

def get_average_grade_student_course (other_list,course):
    all_grades_list_course = [] # Cоздаём пустой список оценок всех студентов конкретного курса
    for student in other_list:
        for key, vul in student.grades_student.items():
            if key == course:
                all_grades_list_course.extend(vul) # Добавим в общий список оценок оценки конкретного студента
    sum_ = sum(all_grades_list_course) # Сумма всех оценок студентов данного курса
    average_grade_student = round(sum_ / len(all_grades_list_course), 2) # Средняя оценка
    return average_grade_student

# Проверка работы функции для подсчёта средней оценки за ДЗ студентов для 2-х курсов :
print(get_average_grade_student_course(student_1.student_list,'Python'))
print(get_average_grade_student_course(student_2.student_list,'Java'))

# Часть 2
# Функция, формирующая список курсов лекторов
def get_lecturer_course(other_list):
    lecturer_course_all = []
    for mentor in other_list:
        if len(mentor.grades_dict_lecturer) > 0: # Убираем проверяющих из списка преподавателей
            lecturer_course_all.extend(mentor.courses_attached)
    lecturer_course_list = list(set(lecturer_course_all))
    return lecturer_course_list
# Проверка
print(get_lecturer_course(Mentor.mentor_list)) # ['Python']

# Функция для подсчета средней оценки за лекции всех лекторов c проверкой
# (в качестве аргумента принимаем список лекторов и название курса)
def get_average_grade_mentor_course (other_list,course):
    # Вызываем список курсов лекторов
    lecturer_course_list = get_lecturer_course(other_list)
    # Проверяем, входит ли подаваемый на вход функции курс в список курсов лекторов
    if course not in lecturer_course_list :
        print('Ошибка.Такого курса нет в списке курсов лекторов')
        return
    all_grades_lecturer_course = [] # Список оценок лекторов
    for lecturer in other_list:
        if len(lecturer.grades_dict_lecturer) > 0:
            for key, vul in lecturer.grades_dict_lecturer.items():
                if key == course:
                    all_grades_lecturer_course.extend(vul) # Заполняем список оценок лекторов
    # Сумма всех оценок лекторов данного курса
    sum_ = sum(all_grades_lecturer_course)
    # Средняя оценка
    average_grade_lecturer = round(sum_ / len(all_grades_lecturer_course), 2)
    return average_grade_lecturer
# Вызываем функцию для подсчета средней оценки за лекции всех лекторов
print(get_average_grade_mentor_course(Mentor.mentor_list,'Python'))
# Проверка при неправильном введении курса :
print(get_average_grade_mentor_course(Mentor.mentor_list,'ython'))