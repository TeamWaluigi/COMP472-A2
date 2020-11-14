from board import Board, get_goal_1, get_goal_2


def h1(board: Board) -> int:
    hamming_distance_goal_1 = hamming_distance(board, get_goal_1(rows=board.rows, columns=board.columns))
    hamming_distance_goal_2 = hamming_distance(board, get_goal_2(rows=board.rows, columns=board.columns))

    if hamming_distance_goal_1 <= hamming_distance_goal_2:
        return hamming_distance_goal_1
    return hamming_distance_goal_2


def h2(board: Board) -> int:
    manhattan_distance_goal_1 = manhattan_distance(board, get_goal_1(rows=board.rows, columns=board.columns))
    manhattan_distance_goal_2 = manhattan_distance(board, get_goal_2(rows=board.rows, columns=board.columns))

    if manhattan_distance_goal_1 <= manhattan_distance_goal_2:
        return manhattan_distance_goal_1
    return manhattan_distance_goal_2


# Used in class as h1 example
# Count number of tiles out of place when compared with goal
def hamming_distance(board: Board, board_goal: Board) -> int:
    score = 0

    for row in range(board_goal.rows):
        for column in range(board_goal.columns):
            tile = board_goal.tiles[row][column]
            actual_row, actual_column = board.get_tile_position(tile)
            goal_row, goal_column = board_goal.get_tile_position(tile)
            if actual_row != goal_row or actual_column != goal_column:
                score += 1

    return score


# Used in class as h2 example
# Sum up all the distances by which tiles are out of place
def manhattan_distance(board: Board, board_goal: Board) -> int:
    score = 0

    for row in range(board_goal.rows):
        for column in range(board_goal.columns):
            tile = board_goal.tiles[row][column]
            actual_row, actual_column = board.get_tile_position(tile)
            goal_row, goal_column = board_goal.get_tile_position(tile)
            score += abs(actual_row - goal_row) + abs(actual_column - goal_column)

    return score

initial_board = Board([4, 2, 3, 1, 5, 6, 7, 0])
initial_board2 = Board([4, 2, 3, 1, 5, 6, 7, 0])
initial_board3 = Board([1, 0, 3, 7, 5, 2, 6, 4])
initial_board4 = Board([3, 2, 5, 1, 6, 4, 7, 0])
initial_board5 = Board([1, 2, 0, 3, 5, 6, 7, 4])
initial_board6 = Board([1, 3, 5, 7, 2, 4, 6, 0])
initial_board7 = Board([0, 3, 7, 5, 2, 6, 1, 4])
initial_board8 = Board([1, 0, 3, 7, 5, 2, 6, 4])
initial_board9 = Board(rows=3, columns=3, raw_board=[1, 7, 3, 4, 5, 6, 2, 8, 0])  # Breaks for now

test_board = initial_board

test_board.print_board()
print(h1(test_board))
print(h2(test_board))

print("----------------------")
print("Completed Board-----------------")
