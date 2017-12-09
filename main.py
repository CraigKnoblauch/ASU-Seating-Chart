from lecturehalls import #Hall
import seating
import sys
import os

try:
    file_name = str(sys.argv[1])
except IndexError:
    sys.exit("\n---- ERROR ----------------------------------------------\n" +
             "- Program accepts .csv files as command line arguments. -\n" +
             "- No arguments were provided.                           -\n" +
             "---------------------------------------------------------\n\n" +
             "Try this: python3 seating_chart.py input.csv\n\n")

if not os.path.isfile(file_name):
    sys.exit("ERROR: File does not exist")

if file_name[-4:] != ".csv":
    sys.exit("\nERROR: Input was not a .csv file\n")

# Make output directory
if not os.path.exists("output"):
    os.makedirs("output")

#NOTE: line 26 to illustrate methodology, does not run, see line 1, 28
hall = HALL()
students = seating.parse_file(file_name)
seating.seat_students(students, hall)
