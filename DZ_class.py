class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []  # Изучаемые на данный момент курсы
        self.grades_student = {}  # Словарь с оценками студента от проверяющих
        self.average_grade = 0  # Средняя оценка за ДЗ
        Student.student_list.append(self)  # Добавляем студента в общий список

    # Метод выставления оценок студентам
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course].append(grade)
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    # Метод для добавления пройденных курсов
    def add_finished_course(self, course_name):
        self.finished_courses.append(course_name)

    # Метод вычисления средней оценки за ДЗ
    def calculate_average_grade(self):
        total_grades = []
        for grades in self.grades_student.values():
            total_grades.extend(grades)

        if total_grades:
            self.average_grade = round(sum(total_grades) / len(total_grades), 2)
        return self.average_grade

    # Магический метод для сравнения студентов по среднему баллу
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade > other.average_grade

    # Метод для представления информации о студенте
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {self.calculate_average_grade()}\n' \
               f'Текущие курсы: {", ".join(self.courses_in_progress)}\n' \
               f'Пройденные курсы: {", ".join(self.finished_courses)}'


# Класс для преподавателей
class Mentor:
    mentors = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Курсы, к которым подключен преподаватель
        Mentor.mentors.append(self)  # Добавляем преподавателя в общий список


# Класс для лекторов, наследуемый от Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}  # Оценки преподавателя от студентов
        self.average_grade = 0  # Средняя оценка за лекции
        Lecturer.mentors.append(self)  # Добавляем лекторов в общий список

    # Метод для вычисления средней оценки за лекции
    def calculate_average_grade(self):
        total_grades = []
        for grades in self.grades_lecturer.values():
            total_grades.extend(grades)

        if total_grades:
            self.average_grade = round(sum(total_grades) / len(total_grades), 2)
        return self.average_grade

    # Магические методы для сравнения лекторов по среднему баллу
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade > other.average_grade

    # Метод для представления информации о преподавателе
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {self.calculate_average_grade()}'

 # Класс для рецензентов, наследуемый от Mentor
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Метод, который позволяет рецензенту добавлять оценку в словарь студента по названию курса:
    def rate_hw(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grades]
            else:
                student.grades_student[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
# Функция для создания списка студентов
def create_students(n):
    students = []
    for i in range(n):
        name = input("Введите имя студента: ")
        surname = input("Введите фамилию студента: ")
        gender = input("Введите пол студента: ")
        student = Student(name, surname, gender)
        students.append(student)

    return students


# Функция для заполнения данных студентов
def fill_students_data(students, courses):
    for student in students:
        student.courses_in_progress = courses
        grades = input(f"Введите оценки для {student.name} через пробел: ").split()
        student.grades_student['course'] = list(map(int, grades))


# Функция для расчета среднего балла по курсу у студентов
def calculate_average_by_course(students, course_name):
    total_grades = []
    for student in students:
        if course_name in student.grades_student:
            total_grades.extend(student.grades_student[course_name])

    if total_grades:
        average_grade = round(sum(total_grades) / len(total_grades), 2)
        return average_grade
    else:
        return None


# Инициализация лекторов :
lecturer_1 = Lecturer('Misha','White')
lecturer_1.courses_attached.append('Python')
lecturer_2 = Lecturer('Anna','Dipl')
lecturer_2.courses_attached.append('Python')
lecturers = [lecturer_1, lecturer_2]
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
student_1.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_1, 'Python', 9)
student_3.rate_hw(lecturer_1, 'Python', 7)
student_4.rate_hw(lecturer_1, 'Python', 8)

student_1.rate_hw(lecturer_2, 'Python', 9)
student_2.rate_hw(lecturer_2, 'Python', 8)
student_3.rate_hw(lecturer_2, 'Python', 5)
student_4.rate_hw(lecturer_2, 'Python', 8)

# Посмотрим оценки обоих лекторов(проверка):
print(lecturer_1.grades_lecturer)
print(lecturer_2.grades_lecturer)
# Вызов метода вычисления средней оценки лекторов
print(lecturer_1.calculate_average_grade())
print(lecturer_2.calculate_average_grade())
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
print(student_1.calculate_average_grade())
print(student_2.calculate_average_grade())
print(student_3.calculate_average_grade())
print(student_4.calculate_average_grade())

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
lecturer_1.average_grade = lecturer_1.calculate_average_grade()
lecturer_2.average_grade = lecturer_2.calculate_average_grade()
print(lecturer_1.average_grade,lecturer_2.average_grade)
# Производим сравнение лекторов по средним оценкам за лекции
print(lecturer_1.average_grade < lecturer_2.average_grade)

# Средние оценки студентов 1 и 2 :
student_1.average_grade = student_1.calculate_average_grade()
student_2.average_grade = student_2.calculate_average_grade()
print(student_1.average_grade,student_2.average_grade)

# Сравним студентов по средней оценке по ДЗ :
print(student_1 > student_2)

#  Функция для подсчета средней оценки за домашние задания по всем
#  студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса)

def get_average_grade_student_course(other_list, course):
    all_grades_list_course = []  # Создаем пустой список оценок всех студентов конкретного курса
    for student in other_list:
        if course in student.grades_student:
            all_grades_list_course.extend(student.grades_student[course])  # Добавим в общий список оценок оценки конкретного студента

    if all_grades_list_course:  # Проверяем, есть ли оценки
        sum_ = sum(all_grades_list_course)  # Сумма всех оценок студентов данного курса
        calculate_average_grade = round(sum_ / len(all_grades_list_course), 2)  # Средняя оценка
        return calculate_average_grade
    else:
        return None  # Если оценок нет, возвращаем None

# Проверка работы функции для подсчёта средней оценки за ДЗ студентов для 2-х курсов :
print(get_average_grade_student_course(student_1.student_list,'Python'))
print(get_average_grade_student_course(student_2.student_list,'Java'))

# Часть 2
# Функция, формирующая список курсов лекторов
def get_lecturer_courses(lecturers):
    lecturer_courses = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            lecturer_courses.extend(lecturer.courses_attached)
    return list(set(lecturer_courses))
# Проверка
lecturer_courses = get_lecturer_courses(lecturers)
print(lecturer_courses)  # ['Python']

# Функция для подсчета средней оценки за лекции всех лекторов c проверкой
# (в качестве аргумента принимаем список лекторов и название курса)
def get_average_grade_mentor_course(mentors, course):
    all_grades_lecturer_course = []  # Список оценок лекторов
    for mentor in mentors:
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached:
            if course in mentor.grades_lecturer:
                all_grades_lecturer_course.extend(mentor.grades_lecturer[course])

    if all_grades_lecturer_course:  # Проверяем, есть ли оценки
        # Сумма всех оценок лекторов данного курса
        sum_ = sum(all_grades_lecturer_course)
        # Средняя оценка
        average_grade_lecturer = round(sum_ / len(all_grades_lecturer_course), 2)
        return average_grade_lecturer
    else:
        return None  # Если оценок нет, возвращаем None
# Рассчитаем среднюю оценку за лекции по курсу 'Python'
average_grade_python = get_average_grade_mentor_course(lecturers, 'Python')
if average_grade_python is not None:
    print(f"Средняя оценка за лекции по курсу 'Python': {average_grade_python}")
else:
    print("Оценок по курсу 'Python' нет.")

# Попробуем рассчитать среднюю оценку за несуществующий курс
average_grade_wrong_course = get_average_grade_mentor_course(lecturers, 'C++')
if average_grade_wrong_course is not None:
    print(f"Средняя оценка за лекции по курсу 'C++': {average_grade_wrong_course}")
else:
    print("Оценок по курсу 'C++' нет.")