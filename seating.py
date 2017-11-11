from lecturehalls import NEEB_HALL
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
    with open(filename) as f:
        row_list = []
        reader = csv.reader(f)
        for row in reader:
            row_str = str(row[first_name_column]).strip() + "|"
            row_str += str(row[last_name_column]).strip() + "|"
            row_str += str(row[pin_column]).strip()

            if "\ufeff" in row_str:
                row_str = row_str.replace("\ufeff", "")

            row_list.append(row_str)

    random.shuffle(row_list)

    return row_list
