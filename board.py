from move import Move


# noinspection DuplicatedCode
def get_goal_1(rows, columns):
    goal_1 = Board(raw_board=range(rows, columns), rows=rows, columns=columns)
    tile = 1

    for row in range(rows):
        for column in range(columns):
            goal_1.tiles[row][column] = tile
            tile += 1
    goal_1.tiles[rows - 1][columns - 1] = 0

    return goal_1


# noinspection DuplicatedCode
def get_goal_2(rows, columns):
    goal_2 = Board(raw_board=range(rows, columns), rows=rows, columns=columns)
    tile = 1

    for column in range(columns):
        for row in range(rows):
            goal_2.tiles[row][column] = tile
            tile += 1
    goal_2.tiles[rows - 1][columns - 1] = 0

    return goal_2


class Board:

    def __init__(self, raw_board, rows=2, columns=4, cost=0, parent=None):
        self.cost = cost
        self.length = rows * columns - 1
        self.rows = rows
        self.columns = columns
        self.parent = parent
        self.tiles = [[0 for _ in range(columns)] for _ in range(rows)]
        self.f = 0
        self.g = 0
        self.h = 0

        row_count = 0
        column_count = 0
        for tile in raw_board:
            self.tiles[row_count][column_count] = tile
            column_count += 1
            if column_count % columns == 0:
                column_count = 0
                row_count += 1

    def raw_board(self):
        board = []
        for row in self.tiles:
            for tile in row:
                board.append(tile)
        return board

    def is_corner_piece(self, row, column):
        if row == 0 or row == self.rows - 1:
            if column == 0 or column == self.columns - 1:
                return True
        return False

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.equals(other)

    def __str__(self):
        representation = ""
        row_string = ""

        for row in self.tiles:
            for tile in row:
                row_string = row_string + " | " + str(tile)
            representation += row_string + "\n"
            row_string = ""

        return representation

    def print_board(self):
        print(self)

    def get_tile_position(self, desired_tile):
        row_count = 0
        column_count = 0
        for row in self.tiles:
            for tile in row:
                if tile == desired_tile:
                    return row_count, column_count
                column_count += 1
            column_count = 0
            row_count += 1

    def get_moves(self):
        row, column = self.get_tile_position(0)
        moves = []

        # Right
        if column + 1 < self.columns:
            moves.append(Move(row, column + 1, row, column, 1 + self.cost))
        # Left
        if column > 0:
            moves.append(Move(row, column - 1, row, column, 1 + self.cost))
        # Up
        if row > 0:
            moves.append(Move(row - 1, column, row, column, 1 + self.cost))
        # Down
        if row + 1 < self.rows:
            moves.append(Move(row + 1, column, row, column, 1 + self.cost))

        if self.is_corner_piece(row, column):

            # Wrapping Moves
            if self.columns > 2:
                # Wrap Left
                if column == 0:
                    moves.append(Move(row, self.columns - 1, row, column, 2 + self.cost))

                # Wrap Right
                if column == self.columns - 1:
                    moves.append(Move(row, 0, row, column, 2 + self.cost))

            if self.rows > 2:
                # Wrap Up
                if row == 0:
                    moves.append(Move(self.rows - 1, column, row, column, 2 + self.cost))

                # Wrap Down
                if row == self.columns - 1:
                    moves.append(Move(0, column, row, column, 2 + self.cost))

            # Immediate Diagonal Moves
            # Up and to the right
            if row > 0 and column + 1 < self.columns:
                moves.append(Move(row - 1, column + 1, row, column, 3 + self.cost))
            # Up and to the left
            if row > 0 and column > 0:
                moves.append(Move(row - 1, column - 1, row, column, 3 + self.cost))
            # Down and to the right
            if row + 1 < self.rows and column + 1 < self.columns:
                moves.append(Move(row + 1, column + 1, row, column, 3 + self.cost))
            # Down and to the left
            if row + 1 < self.rows and column > 0:
                moves.append(Move(row + 1, column - 1, row, column, 3 + self.cost))

            # Opposite Corner Move
            if row == 0:
                # From Top Left
                if column == 0:
                    moves.append(Move(self.rows - 1, self.columns - 1, row, column, 3 + self.cost))
                # From Top Right
                else:
                    moves.append(Move(self.rows - 1, 0, row, column, 3 + self.cost))
            else:
                # From Bottom Left
                if column == 0:
                    moves.append(Move(0, self.columns - 1, row, column, 3 + self.cost))
                # From Bottom Right
                else:
                    moves.append(Move(0, 0, row, column, 3 + self.cost))

        return moves

    #  Just compares the tiles, this is intended
    def equals(self, other_board):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.tiles[row][column] != other_board.tiles[row][column]:
                    return False
        return True

    def get_successors(self):
        successors = []
        moves = self.get_moves()
        raw_board = self.raw_board()

        for move in moves:
            successor = Board(rows=self.rows, columns=self.columns, raw_board=raw_board, cost=move.cost, parent=self)

            zero_row = move.get_zero_row()
            zero_column = move.get_zero_column()
            move_row = move.get_row()
            move_column = move.get_column()
            successor.tiles[zero_row][zero_column], successor.tiles[move_row][move_column] = \
                successor.tiles[move_row][move_column], 0

            successors.append(successor)

        return successors
