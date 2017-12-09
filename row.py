class Row:

    def __init__(self, let='', sn=[], dn=[], sp=-9999):
        self.letter = let.upper()
        self.seat_numbers = sn
        self.assigned_seats = [False] * len(self.seat_numbers)
        self.occupants = [0] * len(self.seat_numbers)  # Will hold Student objects. DO NOT MAKE AN OFF BY ONE ERROR

        self.divided_neighbors = dn

        # Even if you were counting backwards it seems unlikely that there would
        # be 9,999 seats in a row. I don't know why I've just got a feeling
        if sp == -9999:
            self.start_position = self.count_seats() % 2
        else:
            self.start_position = sp

    def add_divided_neighbor(self, sing_dn):
        self.divided_neighbors.append(sing_dn)

    def has_divided_neighbors(self): #NOTE: bring to master
        if self.divided_neighbors:
            return True
        else:
            return False

    def set_start_position(self, start_i):
        self.start_position = start_i

    def get_seat_index(self, seat_number):
        # Assumes that there are no duplicate seat numbers
        return self.seat_numbers.index(seat_number)

    # NOTE: This may need some testing, not sure if you can pass an object as argument that simply.
    def assign_seat(self, seat_number, student_obj):
        self.assigned_seats[self.get_seat_index(seat_number)] = True
        student_obj.seat = self.letter + str(seat_number)
        self.occupants[self.get_seat_index(seat_number)] = student_obj

    # TODO: Implementation waiting for a future update
    def free_seat(self, UNKNOWN):
        pass

    def count_seats(self):
        return len(self.seat_numbers)

    def count_available_seats(self):
        available_seat_count = self.count_seats()

        for b in self.assigned_seats:
            if b:
                available_seat_count -= 1

        return available_seat_count

    # TODO: this needs some testing, but should return the seat numbers of available seats
    def get_available_seat_list(self):
        available_seats = []
        for i in range(0, self.count_seats()):
            if not self.assigned_seats[i]:
                open_seat = self.seat_numbers[i]
                available_seats.append(open_seat)

        return available_seats

    def get_available_seat_indices_list(self):
        aval_seats = self.get_available_seat_list()
        seat_indices = list()
        for seat in aval_seats:
            seat_indices.append(self.get_seat_index(seat))

        return seat_indices
