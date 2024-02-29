

#1
# Импорт модуля csv для работы с файлами CSV
import csv

# Чтение и сохранение содержимого файла 'student_list_27.txt' в виде списка student_list
student_list = list(csv.reader(open('student_list_27.txt')))

# Чтение и сохранение содержимого файла 'class_list_27.txt' в виде списка class_list
class_list = list(csv.reader(open('class_list_27.txt')))

# Определение функции avg_all_credits с двумя аргументами - student_list и class_list
def avg_all_credits(student_list, class_list):
    # Создание пустого словаря для отслеживания суммы кредитов, набранных каждым студентом
    student_credits = {}

    # Начало цикла по каждой строке в student_list
    for st_id, name, year, semest, class_id in student_list:
        # Проверка, есть ли имя студента в словаре student_credits
        if name not in student_credits:
            # Если имя отсутствует, добавляем его в словарь с начальным значением 0
            student_credits[name] = 0

        # Вложенный цикл по каждой строке в class_list
        for cr_id, clas, credit in class_list:
            # Проверка соответствия class_id и cr_id
            if class_id == cr_id:
                # Увеличение суммы кредитов для данного студента на значение credit
                student_credits[name] += int(credit)

    # Вычисление общего количества кредитов (.values() - это значение в словаре )
    total_credits = sum(student_credits.values())

    # Вычисление общего количества студентов
    total_students = len(student_credits)

    # Проверка, если общее количество студентов равно 0, вернуть 0
    if total_students == 0:
        return 0

    # Вычисление среднего количества кредитов
    average_credits = total_credits / total_students

    # Возврат среднего количества кредитов
    return average_credits

# Вызов функции avg_all_credits с передачей аргументов student_list и class_list
result = avg_all_credits(student_list, class_list)

# Вывод результата среднего количества кредитов
print('1) The avg number of credits taken by all students in the dataset: ', result)
print()

#2
credits = [int(credit) for st_id, clas, credit in class_list]

credits.sort()

n = len(credits)
if n % 2 == 0:
    median = (credits[n // 2] + credits[n // 2 - 1 ]) / 2
else:
    median = credits[n // 2]

print('2)',"Median number of class credits : ", median)
print()

#3
def Avg_each_student_credits(student_list, class_list):
    d = {}
    avg = []

    for st_id, name, year, semest, cl_id in student_list:
        for c_id, clas, credit in class_list:
            if name not in d:
                d[name] = []
            if cl_id == c_id and name in d:
                d[name].append(int(credit))

    for i in d:
        avg.append([i, sum(d[i]) // len(d[i])])
    return avg

result = Avg_each_student_credits(student_list, class_list)
print('3)',"Average of total credits each student had:")
for student, average_credits in result:
    print(f"Student Name: {student} | Avg Credits : {average_credits}")
print()

#4

def variance(student_list, class_list):
    d = {}
    for st_id, name, year, semest, cl_id in student_list:
        for c_id, clas, credit in class_list:
            if name not in d:
                d[name] = 0
            if cl_id == c_id and name in d:
                d[name] += int(credit)

    avg = sum(d.values()) / len(d)
    squared_diff = [(avg - val) ** 2 for val in d.values()]
    variance = sum(squared_diff) / len(d)
    standard_deviation = variance ** 0.5
    return standard_deviation

print("4) The variance of total credits taken by students : ", variance(student_list, class_list))
print()

#5

def classes_taken_by_student(student_name, student_list, class_list):
    classes = []
    for st_id, name, year, semest, cl_id in student_list:
        if name == student_name:
            for c_id, clas, credit in class_list:
                if cl_id == c_id:
                    classes.append(clas)
    return classes

student_name = "David Beckham"
classes = classes_taken_by_student(student_name, student_list, class_list)

if classes:
    print('5) Which classes taken , res for one student.')
    print()
    print(f"{student_name} has taken the following classes:")
    for clas in classes:
        print(clas)
print()

#6
print('6)' " The maximum total credits taken by a students so far.")
def max_total_credits(student_list, class_list):
    max_credits = 0
    student_names = []
    total_credits = {}

    for st_id, name, _, _, cl_id in student_list:
        for c_id, _, credit in class_list:
            if cl_id == c_id:
                total_credits[name] = total_credits.get(name, 0) + int(credit)

                if total_credits[name] > max_credits:
                    max_credits = total_credits[name]
                    student_names = [name]
                elif total_credits[name] == max_credits:
                    student_names.append(name)
    if student_names:
        print(f"The students with the maximum total credits are:")
        for student_name in student_names:
            print(f"{student_name}: {max_credits} credits")
    else:
        print("No student records found.")

max_total_credits(student_list, class_list)

print()

#7
print('7)' 'Print the classes that "LeBron James" took in "2023, Spring.')
print()
def find_classes_taken(student_list, class_list, s_name, year, semester):
    classes_taken = []

    for st_id, name, st_year, st_semester, cl_id in student_list:
        if name == student_name and st_year == year and st_semester == semester:
            for c_id, class_name, _ in class_list:
                if cl_id == c_id:
                    classes_taken.append(class_name)

    if classes_taken:
        print(f"{student_name} took this classes in {year}, {semester}:")
        for class_name in classes_taken:
            print(class_name)
    else:
        print("Not found in the list")

student_name = "LeBron James"
year = "2023"
semester = "Spring"

find_classes_taken(student_list, class_list, student_name, year, semester)
print()

#8
print('8) Check attandence of student .')

def did_usain_attend(students, classes, student_name, year, semester):
    for st_id, name, st_year, st_semester, class_id in students:
        if name == student_name and st_year == year and st_semester == semester:
            for cl_id, class_name, credit in classes:
                if cl_id == class_id:
                    return True
    return False

student_name = "Usain Bolt"
year = "2024"
semester = "Spring"
result = did_usain_attend(student_list, class_list, student_name, year, semester)
print(result)
print()

#9
print('9) Who have taken more classes . True if "Maria Sharapova" has taken more classes than "Roger Federer", else, False ')
def more_classes(student_list, student_name1, student_name2):
    count1 = 0
    count2 = 0

    for st_id, name, _, _, class_id in student_list:
        if name == student_name1:
            count1 += 1
        elif name == student_name2:
            count2 += 1

    return count1 > count2

student_name1 = "Maria Sharapova"
student_name2 = "Roger Federer"
result = more_classes(student_list, student_name1, student_name2)

print(result)
print()

#10
print('10) Find if there any students enrolled in the class "2022, Spring".')
print()
def students_enrolled_names(student_list, class_list, year, semester):
    enrolled_students = []
    for st_id, name, st_year, st_semester, class_id in student_list:
        if st_year == year and st_semester == semester:
            enrolled_students.append(name)
    return enrolled_students

year = "2022"
semester = "Spring"
enrolled_student_names = students_enrolled_names(student_list, class_list, year, semester)

if enrolled_student_names:
    print("Students enrolled in", year, semester, "are:" ','.join(enrolled_student_names))

print()

#11
print('11) Find the longest class .')

def find_longest_class_name(class_list):
    longest_class_name = ''
    max_length = 0

    for cl_id, class_name, credit in class_list:
        if len(class_name) > max_length:
            max_length = len(class_name)
            longest_class_name = class_name

    return longest_class_name

longest_class = find_longest_class_name(class_list)

# if longest_class:
print()
print("It is:", longest_class)
    