import copy
import os
import random

file_path = "Input\Puzzles\Puzzles.txt"  # TODO shorten path


def generate_puzzles(row, column, count):
    if os.path.exists(file_path):
        os.remove(file_path)
    f = open(file_path, "x")
    f = open(file_path, "a")
    values = row * column
    possible_tiles = []

    for i in range(values):
        possible_tiles.append(i)

    for i in range(count):
        puzzle_tiles = copy.deepcopy(possible_tiles)
        random.shuffle(puzzle_tiles)
        for j in range(len(puzzle_tiles)):
            f.write(str(puzzle_tiles[j]) + " ")
        f.write("\n")

    f.close()


# generate_puzzles(2, 4, 50)
