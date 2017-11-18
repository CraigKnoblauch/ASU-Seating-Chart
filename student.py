class Student:

    def __init__(self, fn='', ln='', p=0):
        self.first_name = fn
        self.last_name = ln
        self.pin = p
        self.seat = '-0'  # Because a seat named -0 makes no sense

    def assign_seat(self, seat_str):
        self.seat = seat_str

    def is_seated(self):
        return not self.seat == '-0'

    # NOTE: Currently just for trouble shooting
    def print_student(self):
        print(self.first_name + " " + self.last_name + ": " + self.pin)
