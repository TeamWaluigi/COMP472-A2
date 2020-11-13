from board import Board
from search import Search
import time


def h1(board):
    return 1


def h2(board):
    return 1


# Used in class as h2 example
# Sum up all the distances by which tiles are out of place
def manhattan_distance(board):
    return 1


# Used in class as h1 example
# Count number of tiles out of place when compared with goal
def hamming_distance(board):
    return 1