from board import Board, get_goal_1, get_goal_2


# As required
def h0(board: Board) -> int:
    if board.tiles[board.rows - 1][board.columns - 1] == 0:
        return 0
    return 1


def h1(board: Board) -> int:
    hamming_distance_goal_1 = hamming_distance(board, get_goal_1(rows=board.rows, columns=board.columns))
    hamming_distance_goal_2 = hamming_distance(board, get_goal_2(rows=board.rows, columns=board.columns))

    if hamming_distance_goal_1 <= hamming_distance_goal_2:
        return hamming_distance_goal_1
    return hamming_distance_goal_2


def h2(board: Board) -> int:
    manhattan_distance_goal_1 = modified_manhattan_distance(board, get_goal_1(rows=board.rows, columns=board.columns))
    manhattan_distance_goal_2 = modified_manhattan_distance(board, get_goal_2(rows=board.rows, columns=board.columns))

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


# Make a variant of manhattan distance that is admissible
# Sum up all the distances by which tiles are out of place
def modified_manhattan_distance(board: Board, board_goal: Board) -> int:
    score = 0

    for row in range(board_goal.rows):
        for column in range(board_goal.columns):
            tile = board_goal.tiles[row][column]
            actual_row, actual_column = board.get_tile_position(tile)
            goal_row, goal_column = board_goal.get_tile_position(tile)
            tile_score = (abs(actual_row - goal_row) + abs(actual_column - goal_column))
            if tile_score > 2:  # I.e. the cost of a wrapping move, which invalidated the original manhattan distance
                tile_score = 2
            score += tile_score

    return score
