from lecturehalls import NeebHall
from student import Student
import csv
import random
import sys
import math

# NOTE: TODO: Currently no overhead in case the data is input wrong.
# Assuming, data is input as columns: first, last, pin
def parse_file(filename):
    first_name_column = 0
    last_name_column = 1
    pin_column = 2

    # NOTE: No need to check if the file does not exist; that's taken care
    # of in main.py
    with open(filename, "rU") as f:
        student_list = []
        reader = csv.reader(f)
        for row in reader:
            student_obj = Student()

            # Keep input formatting
            student_obj.first_name = str(row[first_name_column]).strip()
            student_obj.last_name = str(row[last_name_column]).strip()
            student_obj.pin = row[pin_column]

            if "\ufeff" in student_obj.first_name:
                student_obj.first_name = student_obj.first_name.replace("\ufeff", "")

            student_list.append(student_obj)

    random.shuffle(student_list)

    return student_list

# TODO: Modify ot produce output csv file
def output_file(students):
    for s in students:
        s.print_student()

# NOTE: Process may not be specific to Austin-Bren-2017F-83238
def seat_students(students, hall):
    updated_students = list()
    start = True

    while len(students) != 0:
        D = len(students) / hall.count_available_seats()  # Density of students per seats
        for hall_row in hall.HALL.values():
            if start:
                i = hall_row.start_position
            else:
                i = 0
            r = D * hall_row.count_available_seats()  # Get the number of students to be seated in this row
            d = hall_row.count_available_seats() / r  # Get the number of seats per students
            aval_seats = hall_row.get_available_seat_list()
            while i < hall_row.count_available_seats():
                try:
                    updated_students.append(students[0])
                    hall_row.assign_seat(aval_seats[math.ceil(i)], students.pop(0))  
                except IndexError:
                    print("All students seated")
                    break
                print("d: " + str(d))
                i += d
                print("i: " + str(i))

        start = False

    output_file(updated_students)
