from move import Move


class Board:

    def __init__(self, row, column, board, cost=0, parent=None):
        row_count = 0
        column_count = 0
        self.cost = cost
        self.length = row * column - 1
        self.row = row
        self.column = column
        self.parent = parent
        self.game_board = [[0 for i in range(column)] for i in range(row)]
        for i in board:
            self.game_board[row_count][column_count] = i
            column_count += 1
            if column_count % column == 0:
                column_count = 0
                row_count += 1

    def return_board(self):
        board = []
        for y in self.game_board:
            for i in y:
                board.append(i)
        return board

    def is_corner_piece(self, row, column):
        if row == 0 or row == self.row - 1:
            if column == 0 or column == self.column - 1:
                return True
        return False

    def print_board(self):
        row = ""
        print("Move cost " + str(self.cost))
        print("Goal State 1: " + str(self.is_goal(2, 4, [1, 2, 3, 4, 5, 6, 7, 0])))
        print("Goal State 2: " + str(self.is_goal(2, 4, [1, 3, 5, 7, 2, 4, 6, 0])))
        # if self.parent != None:
        #     print("Parent " + str(self.parent.PrintBoard()))
        for y in self.game_board:
            for i in y:
                row = row + " | " + str(i)
            print(row)
            row = ""

    def piece_position(self, piece):
        row_count = 0
        column_count = 0
        for y in self.game_board:
            for i in y:
                if i == piece:
                    return row_count, column_count
                column_count += 1
            column_count = 0
            row_count += 1

    def opposite_corner(self):
        row, column = self.piece_position(0)
        array_position = self.length - (row * self.column + column)
        row_count = 0
        if array_position - self.column >= 0:
            row_count += 1
            array_position -= self.column
        column_count = array_position
        return row_count, column_count

    def calculate_moves(self):
        row, column = self.piece_position(0)
        moves = []

        #     Right
        if column + 1 < self.column:
            moves.append(Move(row, column + 1, row, column, 1 + self.cost))
        #     Left
        if column - 1 > -1:
            moves.append(Move(row, column - 1, row, column, 1 + self.cost))
        # Up
        if self.length > row - 1 + column >= 0 and row - 1 > -1:
            moves.append(Move(row - 1, column, row, column, 1 + self.cost))
        #     Down
        if self.length > row + 1 + column >= 0 and row + 1 < self.row:
            moves.append(Move(row + 1, column, row, column, 1 + self.cost))

        if self.is_corner_piece(row, column):

            # End of Same Row Move
            if column == 0:
                moves.append(Move(row, self.column - 1, row, column, 2 + self.cost))
            elif column == self.column - 1:
                moves.append(Move(row, 0, row, column, 2 + self.cost))

            # Immediate Diagonal Moves
            # Up and to the right
            if row - 1 > -1 and column + 1 < self.column:
                moves.append(Move(row - 1, column + 1, row, column, 3 + self.cost))
            # Up and to the left
            if row - 1 > -1 and column - 1 > -1:
                moves.append(Move(row - 1, column - 1, row, column, 3 + self.cost))
            # Down and to the right
            if row + 1 < self.row and column + 1 < self.column:
                moves.append(Move(row + 1, column + 1, row, column, 3 + self.cost))
            # Down and to the left
            if row + 1 < self.row and column - 1 > -1:
                moves.append(Move(row + 1, column - 1, row, column, 3 + self.cost))

            # Absolute Diagonal Move
            opposite_row, opposite_column = self.opposite_corner()
            moves.append(Move(opposite_row, opposite_column, row, column, 3 + self.cost))

        # for i in moves:
            # i.printMoves()

        return moves

    def is_goal(self, row, column, board):
        new_board = Board(row, column, board)
        return self.equals(new_board)

    def equals(self, board2):
        rows = len(self.game_board)
        columns = len(self.game_board[0])
        for i in range(rows):
            for j in range(columns):
                if self.game_board[i][j] != board2.game_board[i][j]:
                    return False
        return True

    def calculate_successors(self):
        boards = []
        moves = self.calculate_moves()
        current_board = self.return_board()

        for i in moves:
            new_board = Board(self.row, self.column, current_board, i.cost, self)
            # temp = new_board.game_board[i.get_row()][i.get_column()]
            # new_board.game_board[i.get_zero_row()][i.get_zero_column()] = temp
            # new_board.game_board[i.get_row()][i.get_column()] = 0

            new_board.game_board[i.get_zero_row()][i.get_zero_column()], new_board.game_board[i.get_row()][i.get_column()] = new_board.game_board[i.get_row()][i.get_column()], 0

            boards.append(new_board)

        return boards


# board = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
# board2 = Board(2, 4, [1, 2, 3, 5, 0, 6, 7, 4])
# board3 = Board(2, 4, [4, 2, 3, 1, 5, 6, 0, 7])
# board4 = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
#
# newboards = board.calculateSuccessors()
#
# second_newboards = newboards[4].calculateSuccessors()
#
# second_newboards[0].PrintBoard()
#
# second_newboards[1].calculateSuccessors()
#
# print(board.isGoal(2, 4, [4, 2, 3, 1, 5, 6, 0, 7]))
