import copy
from typing import List

from move import Move


# noinspection DuplicatedCode
def get_goal_1(rows, columns):
    goal_1 = Board(initializing_input_data=range(rows, columns), rows=rows, columns=columns)
    tile = 1

    for row in range(rows):
        for column in range(columns):
            goal_1.tiles[row][column] = tile
            tile += 1
    goal_1.tiles[rows - 1][columns - 1] = 0

    return goal_1


# noinspection DuplicatedCode
def get_goal_2(rows, columns):
    goal_2 = Board(initializing_input_data=range(rows, columns), rows=rows, columns=columns)
    tile = 1

    for column in range(columns):
        for row in range(rows):
            goal_2.tiles[row][column] = tile
            tile += 1
    goal_2.tiles[rows - 1][columns - 1] = 0

    return goal_2


class Board:

    def __init__(self, tiles_template=None, initializing_input_data=range(2, 4),
                 rows=2, columns=4, g=0, parent=None):
        self.g = g
        self.h = 0
        self.f = 0
        self.execution_time = 0
        self.length = rows * columns - 1
        self.rows = rows
        self.columns = columns
        self.parent = parent
        self.tiles = [[0 for _ in range(columns)] for _ in range(rows)]
        self.last_tile_moved = 0

        if tiles_template is not None:
            self.tiles = tiles_template
        else:
            self.initialize_tiles_using_input_data(columns, initializing_input_data)

    def tiles_to_flat_list(self):
        board = []
        for row in self.tiles:
            for tile in row:
                board.append(tile)
        return board

    def initialize_tiles_using_input_data(self, columns, initializing_input_data):
        row_count = 0
        column_count = 0
        for tile in initializing_input_data:
            self.tiles[row_count][column_count] = tile
            column_count += 1
            if column_count % columns == 0:
                column_count = 0
                row_count += 1

    def is_corner_piece(self, row, column):
        if row == 0 or row == self.rows - 1:
            if column == 0 or column == self.columns - 1:
                return True
        return False

    def __hash__(self):
        hashable_tiles = tuple([tile for row in self.tiles for tile in row])
        return hash(hashable_tiles)

    def __lt__(self, other):
        return self.g < other.g

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
            moves.append(Move(row, column + 1, row, column, 1 + self.g))
        # Left
        if column > 0:
            moves.append(Move(row, column - 1, row, column, 1 + self.g))
        # Up
        if row > 0:
            moves.append(Move(row - 1, column, row, column, 1 + self.g))
        # Down
        if row + 1 < self.rows:
            moves.append(Move(row + 1, column, row, column, 1 + self.g))

        if self.is_corner_piece(row, column):

            # Wrapping Moves
            if self.columns > 2:
                # Wrap Left
                if column == 0:
                    moves.append(Move(row, self.columns - 1, row, column, 2 + self.g))

                # Wrap Right
                if column == self.columns - 1:
                    moves.append(Move(row, 0, row, column, 2 + self.g))

            if self.rows > 2:
                # Wrap Up
                if row == 0:
                    moves.append(Move(self.rows - 1, column, row, column, 2 + self.g))

                # Wrap Down
                if row == self.columns - 1:
                    moves.append(Move(0, column, row, column, 2 + self.g))

            # Immediate Diagonal Moves
            # Up and to the right
            if row > 0 and column + 1 < self.columns:
                moves.append(Move(row - 1, column + 1, row, column, 3 + self.g))
            # Up and to the left
            if row > 0 and column > 0:
                moves.append(Move(row - 1, column - 1, row, column, 3 + self.g))
            # Down and to the right
            if row + 1 < self.rows and column + 1 < self.columns:
                moves.append(Move(row + 1, column + 1, row, column, 3 + self.g))
            # Down and to the left
            if row + 1 < self.rows and column > 0:
                moves.append(Move(row + 1, column - 1, row, column, 3 + self.g))

            # Opposite Corner Move
            if row == 0:
                # From Top Left
                if column == 0:
                    moves.append(Move(self.rows - 1, self.columns - 1, row, column, 3 + self.g))
                # From Top Right
                else:
                    moves.append(Move(self.rows - 1, 0, row, column, 3 + self.g))
            else:
                # From Bottom Left
                if column == 0:
                    moves.append(Move(0, self.columns - 1, row, column, 3 + self.g))
                # From Bottom Right
                else:
                    moves.append(Move(0, 0, row, column, 3 + self.g))

        return moves

    def equals(self, other_board):
        return hash(self) == hash(other_board)

    def get_successors(self):
        successors = []
        moves = self.get_moves()

        for move in moves:
            tiles_template = copy.deepcopy(self.tiles)
            successor = Board(rows=self.rows, columns=self.columns, tiles_template=tiles_template,
                              g=move.cost, parent=self)

            zero_row = move.get_zero_row()
            zero_column = move.get_zero_column()
            move_row = move.get_row()
            move_column = move.get_column()
            successor.last_tile_moved = successor.tiles[move_row][move_column]
            successor.tiles[zero_row][zero_column], successor.tiles[move_row][move_column] = \
                successor.tiles[move_row][move_column], 0

            successors.append(successor)

        return successors
