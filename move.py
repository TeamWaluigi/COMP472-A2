class Move:

    def __init__(self, row, column, ZeroRow, ZeroColumn, cost=0):
        self.row = row
        self.column = column
        self.ZeroRow = ZeroRow
        self.ZeroColumn = ZeroColumn
        self.cost = cost

    def printMoves(self):
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
