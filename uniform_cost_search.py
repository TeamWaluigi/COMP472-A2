from board import Board
from search import Search
import time

parent_board = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
parent_board2 = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
parent_board3 = Board(2, 4, [1, 0, 3, 7, 5, 2, 6, 4])
parent_board4 = Board(2, 4, [3, 2, 5, 1, 6, 4, 7, 0])
parent_board5 = Board(2, 4, [1, 2, 0, 3, 5, 6, 7, 4])
parent_board6 = Board(2, 4, [1, 3, 5, 7, 2, 4, 6, 0])
parent_board7 = Board(2, 4, [0, 3, 7, 5, 2, 6, 1, 4])
parent_board8 = Board(2, 4, [1, 0, 3, 7, 5, 2, 6, 4])

currentview = parent_board
goal1 = [1, 2, 3, 4, 5, 6, 7, 0]
goal2 = [1, 3, 5, 7, 2, 4, 6, 0]


def findGoalState(board):
    start = time.time()
    currentview = board
    currentview.PrintBoard()
    search = Search(board)
    while not currentview.isGoal(2, 4, goal1) and not currentview.isGoal(2, 4, goal2):
        children = currentview.calculateSuccessors()
        search.AddNewChildren(children)
        if len(search.unvisited) > 0:
            currentview = search.unvisited.pop(0)
            search.visited.append(currentview)
    print(search.unvisited.__len__())
    print(search.visited.__len__())
    end = time.time()
    print(end - start)
    return currentview






goalstate = findGoalState(parent_board)
print("----------------------")
print("----------------------")
goalstate.PrintBoard()

