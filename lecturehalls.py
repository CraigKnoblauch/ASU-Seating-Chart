# Module for holding Lecture Hall classes. If this program ever needs to be expanded,
# a lecture hall can be added here as a class.
#
# The resulting HALL member is in this format:
#
# {'Row Letter': [ [least_seat_number, ... , greatest_seat_number],
#                  Boolean to denote if there are divided neignbors,
#                  [ [divided_seat_number 1, divided_seat_number2], [divided_seat_number1, 2, divided_seat_number3] ]
#                ]
# }
def make_row(letter, seat_numbers, divided_neighbors_exist=False, divided_neighbors=[]):
    row = [letter.upper()]

    for sn in seat_numbers:
        row.append(sn)

    sn.append(divided_neighbors_exist)

    if divided_neighbors_exist:
        for dn in divided_neighbors:
            sn.append(dn)


def make_hall(rows):
    hall = {}
    for r in rows:
        row_key = r.pop(0)
        hall[row_key] = r
        

class NeebHall:
    def __init__(self):
        self.B_ROW = make_row('B', list(range(1, 23+1)))
        self.C_ROW = make_row('C', list(range(1, 26+1)))
        self.D_ROW = make_row('D', list(range(1, 27+1)))
        self.E_ROW = make_row('E', list(range(1, 29+1)))
        self.F_ROW = make_row('F', list(range(1, 31+1)))
        self.G_ROW = make_row('G', list(range(1, 33+1)))
        self.H_ROW = make_row('H', list(range(1, 35+1)))
        self.J_ROW = make_row('J', list(range(1, 37+1)))
        self.K_ROW = make_row('K', list(range(1, 38+1)))
        self.L_ROW = make_row('L', list(range(1, 40+1)))
        self.M_ROW = make_row('M', list(range(1, 41+1)))
        self.N_ROW = make_row('N', list(range(1, 37+1)))
        self.O_ROW = make_row('O', [1, 2, 3, 4, 5, 6, 7, 8, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], True, [[8,27]])
        self.P_ROW = make_row('P', [1, 2, 3, 4, 5, 6, 7, 8, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], True, [[8,27]])

        self.HALL = make_hall([B_ROW, C_ROW, D_ROW, E_ROW, F_ROW, G_ROW, H_ROW, J_ROW, K_ROW, L_ROW, M_ROW, N_ROW, O_ROW, P_ROW])
