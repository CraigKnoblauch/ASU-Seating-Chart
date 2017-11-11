# Module for holding Lecture Hall classes. If this program ever needs to be expanded,
# a lecture hall can be added here as a class.


class Row:

    def __init__(self, let='', sn=[], dn=[]):
        self.letter = let
        self.seat_numbers = sn
        self.divided_neighbors = dn
        self.taken_seats = [False for i in self.seat_numbers]

    def add_divided_neighbor(self, sing_dn):
        self.divided_neighbors.append(sing_dn)


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
        self.O_ROW = Row(let= 'O', sn= [1, 2, 3, 4, 5, 6, 7, 8, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], dn= [[8,27]])
        self.P_ROW = Row(let= 'P', sn= [1, 2, 3, 4, 5, 6, 7, 8, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], dn= [[8,27]])

        self.HALL = [B_ROW, C_ROW, D_ROW, E_ROW, F_ROW, G_ROW, H_ROW, J_ROW, K_ROW, L_ROW, M_ROW, N_ROW, O_ROW, P_ROW]
