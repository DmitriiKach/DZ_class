class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        self.average_grade = 0
    def grades_for_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
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
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades_lecturer = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecturer = {}

    def average_grade_lectures(self):
        grade_list = []
        for val in self.grades_lecturer.values():
            grade_list.extend(val)
        # Подсчитаем сумму оценок:
        sum_ = sum(grade_list)
        # Подсчитаем среднее значение всех оценок
        self.average_grade = round(sum_ / len(grade_list), 2)
        return self.average_grade

        #  Метод сравнения средних оценок лекторов :
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
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f' Имя: {self.name} \n Фамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java']
# best_student.finished_courses += ['Java']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_lecturer = Lecturer('Ivan', 'Kick')
cool_lecturer.courses_attached += ['Python', 'Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
best_student.grades_for_lecturer(cool_lecturer, 'Java', 8)
best_student.grades_for_lecturer(cool_lecturer, 'Java', 9)
best_student.grades_for_lecturer(cool_lecturer, 'Java', 10)

print(best_student.grades_student)
print(cool_lecturer.grades_lecturer)
print(cool_reviewer)

# Инициализация лекторов :
lecturer_1 = Lecturer('Misha','White')
lecturer_1.courses_attached.append('Python')
lecturer_2 = Lecturer('Anna','Dipl')
lecturer_2.courses_attached.append('Python')
# Инициализация студентов :
student_1= Student('Vasya','Nogh','Male')
student_1.courses_in_progress.append('Python')
student_2= Student('Maria','Rich','Female')
student_2.courses_in_progress.append('Python')
student_3= Student('Elena','Gray','Female')
student_3.courses_in_progress.append('Python')
# Выставим оценки лектору-1
student_1.grades_for_lecturer(lecturer_1, 'Python', 9)
student_2.grades_for_lecturer(lecturer_1, 'Python', 9)
student_3.grades_for_lecturer(lecturer_1, 'Python', 7)
# Выставим оценки лектору-2
student_1.grades_for_lecturer(lecturer_2, 'Python', 9)
student_2.grades_for_lecturer(lecturer_2, 'Python', 8)
student_3.grades_for_lecturer(lecturer_2, 'Python', 5)
# Посмотрим оценки обоих лекторов(проверка):
print(lecturer_1.grades_lecturer)
print(lecturer_2.grades_lecturer)
# Вызов метода вычисления средней оценки лектора_1
print(lecturer_1.average_grade_lectures())
print(lecturer_1)
print(lecturer_2)

# Инициализируем проверяющих
reviewer_1 = Reviewer ('Petr','Maksimov')
reviewer_1.courses_attached.append('Python') # Добавили курс 'Python' в список проверяемых курсов
# Зададим выставление оценок проверяющими (reviewer) студентам соответствующих курсов
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 6)
print(f'Оценки для {student_1.name} - {student_1.grades_student }')
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Python', 6)
print(f'Оценки для {student_2.name} - {student_2.grades_student }')
# Проверка - Средняя оценка для student_1:
print(student_1.average_grade)
# Добавим курс в список текущих курсов
student_1.courses_in_progress.append('Git')
print(student_1.courses_in_progress)
# Добавим курс в список оконченных курсов :
student_1.finished_courses.append('Введение в программирование')
# Проверка переопределения метода __str__ для студентов:
print(student_1)

# 2) Реализуйте возможность сравнивать (через операторы сравнения)
# между собой лекторов по средней оценке за лекции и студентов по
# средней оценке за домашние задания.

# Проверим словари с оценками у лекторов:
print (lecturer_1.grades_lecturer) # {'Python': [9, 9, 10]}
print (lecturer_2.grades_lecturer) # {'Python': [9, 8, 8]}
# Средние оценки лекторов 1 и 2 :
lecturer_1.average_grade = lecturer_1.average_grade_lectures()
lecturer_2.average_grade = lecturer_2.average_grade_lectures()
print(lecturer_1.average_grade,lecturer_2.average_grade) # 9.33 8.33
# Производим сравнение лекторов по средним оценкам за лекции
print(lecturer_1 < lecturer_2) # False

# Средние оценки студентов 1 и 2 :
student_1.average_grade = student_1.average_grade_student()
student_2.average_grade = student_2.average_grade_student()
print(student_1.average_grade,student_2.average_grade) # 9.67 8.67
# Сравним студентов по средней оценке по ДЗ :
print(student_1 > student_2) # True