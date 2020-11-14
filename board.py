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

    def print_board(self):
        row_string = ""
        for row in self.tiles:
            for tile in row:
                row_string = row_string + " | " + str(tile)
            print(row_string)
            row_string = ""

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

    def get_opposite_corner_tile_position(self):
        row, column = self.get_tile_position(0)
        array_position = self.length - (row * self.columns + column)
        row_count = 0
        if array_position - self.columns >= 0:
            row_count += 1
            array_position -= self.columns
        column_count = array_position
        return row_count, column_count

    def calculate_moves(self):
        row, column = self.get_tile_position(0)
        moves = []

        #     Right
        if column + 1 < self.columns:
            moves.append(Move(row, column + 1, row, column, 1 + self.cost))
        #     Left
        if column - 1 > -1:
            moves.append(Move(row, column - 1, row, column, 1 + self.cost))
        # Up
        if self.length > row - 1 + column >= 0 and row - 1 > -1:
            moves.append(Move(row - 1, column, row, column, 1 + self.cost))
        #     Down
        if self.length > row + 1 + column >= 0 and row + 1 < self.rows:
            moves.append(Move(row + 1, column, row, column, 1 + self.cost))

        if self.is_corner_piece(row, column):

            # End of Same Row Move
            if column == 0:
                moves.append(Move(row, self.columns - 1, row, column, 2 + self.cost))
            elif column == self.columns - 1:
                moves.append(Move(row, 0, row, column, 2 + self.cost))

            # Immediate Diagonal Moves
            # Up and to the right
            if row - 1 > -1 and column + 1 < self.columns:
                moves.append(Move(row - 1, column + 1, row, column, 3 + self.cost))
            # Up and to the left
            if row - 1 > -1 and column - 1 > -1:
                moves.append(Move(row - 1, column - 1, row, column, 3 + self.cost))
            # Down and to the right
            if row + 1 < self.rows and column + 1 < self.columns:
                moves.append(Move(row + 1, column + 1, row, column, 3 + self.cost))
            # Down and to the left
            if row + 1 < self.rows and column - 1 > -1:
                moves.append(Move(row + 1, column - 1, row, column, 3 + self.cost))

            # Absolute Diagonal Move
            opposite_row, opposite_column = self.get_opposite_corner_tile_position()
            moves.append(Move(opposite_row, opposite_column, row, column, 3 + self.cost))

        # for i in moves:
        # i.printMoves()

        return moves

    def equals(self, other_board):
        rows = len(self.tiles)
        columns = len(self.tiles[0])
        for row in range(rows):
            for column in range(columns):
                if self.tiles[row][column] != other_board.tiles[row][column]:
                    return False
        return True

    def calculate_successors(self):
        boards = []
        moves = self.calculate_moves()
        current_board = self.raw_board()

        for i in moves:
            new_board = Board(rows=self.rows, columns=self.columns, raw_board=current_board, cost=i.cost, parent=self)
            # temp = new_board.game_board[i.get_row()][i.get_column()]
            # new_board.game_board[i.get_zero_row()][i.get_zero_column()] = temp
            # new_board.game_board[i.get_row()][i.get_column()] = 0

            new_board.tiles[i.get_zero_row()][i.get_zero_column()], new_board.tiles[i.get_row()][
                i.get_column()] = new_board.tiles[i.get_row()][i.get_column()], 0

            boards.append(new_board)

        return boards
