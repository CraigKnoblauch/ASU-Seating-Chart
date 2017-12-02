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

# NOTE: Process specific to Austin-Bren-2017F-83238, should not be used in full in other versions
def seat_students(students, hall):
    updated_students = list()

    # NOTE: Testing linear fill - SUCCESS
    # i = 0
    # for hall_row in hall.HALL.values():
    #     for seat in hall_row.get_available_seat_list():
    #         try:
    #             hall_row.assign_seat(seat, students[i])
    #         except IndexError:
    #             break
    #         i += 1

    # NOTE: Support for divided_neighbors not added because it is not needed in this branches case
    # First round of seating. Each student is placed with one seat in between them,
    # starting at the row's start_position
    # NOTE: This first process may be able to be ported over to master
    for hall_row in hall.HALL.values():
        break_after = False
        pos = hall_row.start_position
        while True:
            try:
                students[0]
            except IndexError:
                print("All students seated")
                break

            try:
                updated_students.append(students[0])
                hall_row.assign_seat(hall_row.seat_numbers[pos],
                                     students.pop(0))
            except IndexError:
                print("seat_numbers index error")
                break

            pos += 2

            try:
                if break_after:
                    break
                if hall_row.seat_numbers[pos] == hall_row.seat_numbers[-2] or hall_row.seat_numbers[pos] == hall_row.seat_numbers[-1]:
                    break_after = True
            except IndexError:
                print("Index error in seat_students triggered")
                break
    # # NOTE
    # # NOTE: The following lines follow heavy assumptions that ONLY APPLY TO THIS BRANCH. If any of this code is brought to master is should be strongly cherry picked
    # # NOTE
    # #
    # # TODO: Next step, divide remaining students among rows
    # remaining_student_N = len(students[student_index:]))
    #
    # #TODO: Seat these students in a binary fashion
    # students_per_row = remaining_student_N // hall.count_rows()  #NOTE: Assumes a non zero result as will be the case in this branch ONLY
    # for hall_row in hall.HALL.values():
    #     aval_seats = hall_row.get_available_seat_list()
    #     aval_seats_N = len(aval_seats)
    #
    #
    # remaining_student_N = remaining_student_N % hall.count_rows()

    output_file(updated_students)
