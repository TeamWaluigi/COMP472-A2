from board import Board
from search import Search

parent_board = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
search = Search(parent_board)
currentview = parent_board
goal1 = [1, 2, 3, 4, 5, 6, 7, 0]
goal2 = [1, 3, 5, 7, 2, 4, 6, 0]


def findGoalState(board):
    currentview = board
    currentview.PrintBoard()
    # while currentview.isGoal(2, 4, goal1) != True and currentview.isGoal(2, 4, goal2) != True:
    for x in range(100):
        children = currentview.calculateSuccessors()
        search.AddNewChildren(children)
        search.SortByMoveCost()
        if search.unvisited.__len__() > 0:
            currentview = search.unvisited.pop(0)
            search.visited.append(currentview)
        search.PrintLists()

    return True, currentview


goalstate = findGoalState(parent_board)
# goalstate.PrintBoard()
