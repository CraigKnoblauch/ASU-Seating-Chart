# Module for holding Lecture Hall classes. If this program ever needs to be expanded,
# a lecture hall can be added here as a class.


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
            self.start_position = self.count_seats() % 2 #NOTE: bring to master
        else:
            self.start_position = sp

    def add_divided_neighbor(self, sing_dn):
        self.divided_neighbors.append(sing_dn)

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


class NeebHall:

    def __init__(self):
        # self.A_ROW = Row(let= 'A', sn= [1,2,3,4,5,6], dn=[3,4])  # NOTE: Should be commented out on Austin-Bren-2017F-83238 branch
        self.B_ROW = Row(let= 'B', sn= list(range(1, 23+1)) )
        self.C_ROW = Row(let= 'C', sn= list(range(1, 26+1)) )
        self.D_ROW = Row(let= 'D', sn= list(range(1, 27+1)) )
        self.E_ROW = Row(let= 'E', sn= list(range(1, 29+1)) )
        self.F_ROW = Row(let= 'F', sn= list(range(1, 31+1)) )
        self.G_ROW = Row(let= 'G', sn= list(range(1, 33+1)) )
        self.H_ROW = Row(let= 'H', sn= list(range(1, 35+1)) )
        self.J_ROW = Row(let= 'J', sn= list(range(1, 37+1)) )
        self.K_ROW = Row(let= 'K', sn= list(range(1, 38+1)) )
        self.L_ROW = Row(let= 'L', sn= list(range(1, 40+1)) )
        self.M_ROW = Row(let= 'M', sn= list(range(1, 41+1)) )
        self.N_ROW = Row(let= 'N', sn= list(range(1, 37+1)) )
        self.O_ROW = Row(let= 'O', sn= [1, 2, 3, 4, 5, 6, 7, 8, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], dn= [[8,27]], sp=1)
        self.P_ROW = Row(let= 'P', sn= [1, 2, 3, 4, 5, 6, 7, 8, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], dn= [[8,27]], sp=1)

        self.HALL = {'B': self.B_ROW, 'C': self.C_ROW, 'D': self.D_ROW,
                     'E': self.E_ROW, 'F': self.F_ROW, 'G': self.G_ROW,
                     'H': self.H_ROW, 'J': self.J_ROW, 'K': self.K_ROW,
                     'L': self.L_ROW, 'M': self.M_ROW, 'N': self.N_ROW,
                     'O': self.O_ROW, 'P': self.P_ROW }

        self.seat_count = 0
        for row in self.HALL.values():
            self.seat_count += row.count_seats()
