from board import Board
from search import Search
import time

parent_board = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
parent_board2 = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
parent_board3 = Board(2, 4, [1, 0, 3, 7, 5, 2, 6, 4])
parent_board4 = Board(2, 4, [3, 2, 5, 1, 6, 4, 7, 0])
parent_board5 = Board(2, 4, [1, 2, 0, 3, 5, 6, 7, 4])
parent_board6 = Board(2, 4, [1, 3, 5, 7, 2, 4, 6, 0])
currentview = parent_board
goal1 = [1, 2, 3, 4, 5, 6, 7, 0]
goal2 = [1, 3, 5, 7, 2, 4, 6, 0]


def findGoalState(board):
    start = time.time()
    successors = 0
    newchildren = 0
    movecosttime = 0
    currentview = board
    currentview.PrintBoard()
    search = Search(board)
    while not currentview.isGoal(2, 4, goal1) and not currentview.isGoal(2, 4, goal2):
        startsuccessors = time.time()
        children = currentview.calculateSuccessors()
        endsuccessors = time.time()
        successors = successors + endsuccessors - startsuccessors
        startchildren = time.time()
        search.AddNewChildren(children)
        endchildren = time.time()
        newchildren = newchildren + endchildren - startchildren
        # startmove = time.time()
        # search.SortByMoveCost()
        # endmove = time.time()
        # movecosttime = movecosttime + endmove - startmove
        if len(search.unvisited) > 0:
            currentview = search.unvisited.pop(0)
            search.visited.append(currentview)
        # if currentview.isGoal(2, 4, [1, 2, 3, 4, 5, 6, 7, 0]):
        #     return currentview
        # if currentview.isGoal(2, 4, [1, 3, 5, 7, 2, 4, 6, 0]):
        #     return currentview
    print(search.unvisited.__len__())
    print(search.visited.__len__())
    end = time.time()
    print(successors)
    print(newchildren)
    print(movecosttime)
    return currentview






goalstate = findGoalState(parent_board4)
print("----------------------")
print("----------------------")
goalstate.PrintBoard()
print("----------------------")
print("----------------------")
parent_board6.PrintBoard()
