    # 11.10.2023 home work 1 
import csv


def avg_time(arr):
    if len(arr):
        s = 0
        for hour, minute in arr:
            s += int(hour) * 60 + int(minute)
        avg = s / len(arr)
        hours = int(avg / 60)
        mins = int(avg % 60)
        hours = hours if hours > 9 else "0" + str(hours)
        mins = mins if mins > 9 else "0" + str(mins)
        return f"{hours}:{mins}"


def late_count(arr, time):
    count = 0
    if len(arr):
        hour, minute = time.split(":")
        threshold = int(hour) * 60 + int(minute)
        for hour, minute in arr:
            t = hour * 60 + minute
            if t > threshold:
                count += 1
        return count


def who_was_late(arr, time, input_date):
    print("LATE STUDENTS", input_date)
    hour, minute = time.split(":")
    threshold = int(hour) * 60 + int(minute)
    for name, date, time in arr:
        hour, minute = time.split(":")
        t = int(hour) * 60 + int(minute)
        if input_date == date and t > threshold:
            print(name, time)
    print("")


def get_attend_dates(arr, student_name):
    attended_dates = set()
    for name, date, time in arr:
        if name == student_name:
            attended_dates.add(date)
    return attended_dates


def filter_table(arr, student_name):
    sub_arr = []
    attended_dates = set()
    print(f"{student_name} stats:")
    for name, date, time in arr:
        if name == student_name:
            hour, minute = time.split(":")
            sub_arr.append((int(hour), int(minute)))
            attended_dates.add(date)
    missed_dates = dates - attended_dates
    if missed_dates:
        print("missed dates:", ", ".join(missed_dates))
    else:
        print("no missed dates")
    print(f"attendance: {int((len(attended_dates) / len(dates)) * 100)}%")
    print("avg time:", avg_time(sub_arr))
    print("was late", late_count(sub_arr, "10:00"), "times")
    print("")


def general_stats(students, timetable, dates):
    print("GENERAL STUDENT STATS")
    print(
        "average time:",
        avg_time([time.split(":") for name, date, time in timetable]),
    )
    who_lates_the_most(students, timetable)
    who_attends_the_most(students, timetable, dates)
    highest_and_lowest_attendance(timetable, dates)


def who_was_in(timetable, qtime, qdate):
    qtimes = [int(i) for i in qtime.split(":")]
    qtimes = qtimes[0] * 60 + qtimes[1]
    count = 0
    for name, date, time in timetable:
        if qdate == date:
            time = [int(i) for i in time.split(":")]
            time = time[0] * 60 + time[1]
            if time <= qtimes:
                count += 1
    print(f"{qdate} at {qtime} {count} students were in the class")


def who_lates_the_most(students, timetable):
    late_count = [0 for name in students]
    for name, date, time in timetable:
        time = [int(i) for i in time.split(":")]
        if time[0] >= 10 and time[1] > 0:
            late_count[students.index(name)] += 1
    mx = max(zip(late_count, students))
    print(f"{mx[1]} was late most often, he/she was late {mx[0]} times")


def who_attends_the_most(students, timetable, dates):
    wasnt = [0 for name in students]
    for student in students:
        attended = get_attend_dates(timetable, student)
        for idate in dates:
            if idate not in attended:
                wasnt[students.index(student)] += 1
    wasnt = min([[count, name] for count, name in zip(wasnt, students)])
    print(f"{wasnt[1]} attends the most, he/she missed {wasnt[0]} classes")


def highest_and_lowest_attendance(timetable, dates):
    dates = list(dates)
    attendance = [0 for i in dates]
    for name, date, time in timetable:
        attendance[dates.index(date)] += 1
    attended = [[attd, date] for attd, date in zip(attendance, dates)]
    mx = max(attended)
    mn = min(attended)
    print(f"Highest attendent was {mx[1]}, {mx[0]} students was attended")
    print(f"Lowest attendent was {mn[1]}, {mn[0]} students was attended")


def get_stats(students, timetable, dates):
    for student_name in students:
        filter_table(timetable, student_name)

    who_was_late(timetable, "10:05", "10-10-2023")

    general_stats(students, timetable, dates)

    who_was_in(timetable, "10:08", "10-11-2023")


timetable = [
    [name, date, time] for i, name, date, time in csv.reader(open("university.txt"))
]
students = [name for i, name in csv.reader(open("student_list.txt"))]
dates = set([date for name, date, time in timetable])

get_stats(students, timetable, dates)



## home work 2 (10-11-2023   10:08)

import csv 

university = csv.reader(open('university.txt', "r"))

def who_was_not_late(arr, input_date, input_time):
    count = 0 
    
    for id, name, date, time in university:
        if date == input_date and input_time >= time:
            count += 1
            print(name)
    return count       
print(who_was_not_late(university, '10-11-2023','10:08'))