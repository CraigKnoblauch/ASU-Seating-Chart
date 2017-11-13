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
