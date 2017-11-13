# Module for holding Lecture Hall classes. If this program ever needs to be expanded,
# a lecture hall can be added here as a class.


class Row:

    def __init__(self, let='', sn=[], dn=[], sp=0):
        self.letter = let
        self.seat_numbers = sn
        self.assigned_seats = [False] * len(self.seat_numbers)
        self.occupants = [0] * len(self.seat_numbers)  # Will hold Student objects. DO NOT MAKE AN OFF BY ONE ERROR

        self.divided_neighbors = dn
        self.start_position = sp

    def add_divided_neighbor(self, sing_dn):
        self.divided_neighbors.append(sing_dn)

    def set_start_position(self, start_i):
        self.start_position = start_i

    def assign_seat(self, seat):
        self.assigned_seats[seat-1] = True

    def free_seat(self, seat):
        self.assigned_seats[seat-1] = False

    def count_seats(self):
        return len(self.seat_numbers)


class NeebHall:

    def __init__(self):
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
