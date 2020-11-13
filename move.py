class Move:

    def __init__(self, row, column, zero_row, zero_column, cost=0, total_cost=0):
        self.row = row
        self.column = column
        self.ZeroRow = zero_row
        self.ZeroColumn = zero_column
        self.cost = cost
        self.total_cost = total_cost

    def print_moves(self):
        print("Move from (" + str(self.ZeroRow) + "," + str(self.ZeroColumn) + ") to (" + str(self.row) + ","
              + str(self.column) + ")")

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_zero_row(self):
        return self.ZeroRow

    def get_zero_column(self):
        return self.ZeroColumn
