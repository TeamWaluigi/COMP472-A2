from typing import List

default_puzzle_file_path = "C:\Git Repositories\COMP472-A2\Input\Puzzles\Puzzles.txt"


def get_puzzles_from_file(puzzle_file_path=default_puzzle_file_path) -> any:
    puzzle_file = open(puzzle_file_path, "r")
    puzzle_lines = puzzle_file.readlines()
    puzzles = []

    for puzzle_line in puzzle_lines:
        puzzle = [int(tile) for tile in puzzle_line.strip().split(' ')]
        puzzles.append(puzzle)

    return puzzles


# result = get_puzzles_from_file()
# print(result)
