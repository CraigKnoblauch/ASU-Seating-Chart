from lecturehalls import NeebHall
from student import Student
import csv
import random
import sys

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

# Process specific to Austin-Bren-2017F-83238, should not be used in full in other versions
def seat_students(students, hall):
    N_seats = hall.seat_count
    N_students = len(students)

    # NOTE: Testing linear fill - SUCCESS
    # i = 0
    # for hall_row in hall.HALL.values():
    #     for seat in hall_row.get_available_seat_list():
    #         try:
    #             hall_row.assign_seat(seat, students[i])
    #         except IndexError:
    #             break
    #         i += 1

    output_file(students)
