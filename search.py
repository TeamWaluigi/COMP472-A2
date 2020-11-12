from board import Board


class Search:

    def __init__(self, board, visited=[], unvisited=[]):
        self.visited = visited
        self.visited.append(board)
        self.unvisited = unvisited

    def visit(self, board):
        self.visited.append(board)
        self.RefreshUnvisited()

    def AddNewChildren(self, new_boards):
        for board in new_boards:
            self.unvisited.append(board)
        self.RefreshUnvisited()

    def RefreshUnvisited(self):
        visited = self.visited
        unvisited = self.unvisited
        for visited_board in visited:
            for unvisited_board in unvisited:
                if visited_board.equals(unvisited_board):
                    self.unvisited.remove(unvisited_board)

    def SortByMoveCost(self):
        for i in range(len(self.unvisited)):
            for j in range(len(self.unvisited) - 1):
                if self.unvisited[j].cost > self.unvisited[j + 1].cost:
                    self.unvisited[j], self.unvisited[j + 1] = self.unvisited[j + 1], self.unvisited[j]

    def PrintLists(self):
        print("------------------------------")
        print("Visited:")
        for board in self.visited:
            print(board.returnBoard())
        print("Unvisited")
        for board in self.unvisited:
            print(board.returnBoard())
        print("------------------------------")
        print("")
        print("")
        print("")


parent_board = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])

child_boards1 = [
Board(2, 4, [0, 2, 3, 1, 5, 6, 7, 4], 3, parent_board),
Board(2, 4, [4, 2, 3, 1, 0, 6, 7, 5], 2, parent_board),
Board(2, 4, [4, 2, 0, 1, 5, 6, 7, 3], 3, parent_board),
Board(2, 4, [4, 2, 3, 0, 5, 6, 7, 1], 1, parent_board),
Board(2, 4, [4, 2, 3, 1, 5, 6, 0, 7], 1, parent_board),
]

child_boards2 = [
Board(2, 4, [4, 2, 0, 1, 5, 6, 3, 7], 1, child_boards1[4]),
Board(2, 4, [4, 2, 3, 1, 5, 0, 6, 7], 1, child_boards1[4]),
Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0], 1, child_boards1[4]),
]

search = Search(parent_board)
search.AddNewChildren(child_boards1)
search.PrintLists()
search.visit(Board(2, 4, [4, 2, 3, 1, 5, 6, 0, 7]))
search.AddNewChildren(child_boards2)
search.PrintLists()
search.SortByMoveCost()
search.PrintLists()

