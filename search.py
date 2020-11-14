from board import Board


class Search:

    def __init__(self, board, visited=None, unvisited=None):
        if unvisited is None:
            unvisited = []
        if visited is None:
            visited = []
        self.visited = visited
        self.visited.append(board)
        self.unvisited = unvisited

    def visit(self, board):
        self.visited.append(board)
        for existing_board in self.unvisited:
            if board.equals(existing_board):
                self.unvisited.remove(existing_board)

    def add_new_children(self, new_boards):
        for board in new_boards:
            flag = True
            for existing_board in self.unvisited:
                if board.equals(existing_board):
                    if board.cost < existing_board.cost:
                        self.unvisited.remove(existing_board)
                        self.add_child(board)
                    flag = False
            for existing_board in self.visited:
                if board.equals(existing_board):
                    flag = False
            if flag:
                self.add_child(board)

    def refresh_unvisited(self):
        visited = self.visited
        unvisited = self.unvisited
        for visited_board in visited:
            for unvisited_board in unvisited:
                if visited_board.equals(unvisited_board):
                    self.unvisited.remove(unvisited_board)

    def add_child(self, board):
        for count in range(len(self.unvisited)):
            if board.cost <= self.unvisited[count].cost:
                self.unvisited.insert(count, board)
                return
        self.unvisited.append(board)

    # TODO may be convenient to use for other methods?
    def sort_by_move_cost(self):
        self.unvisited.sort(key=lambda move: move.cost)

    def print_lists(self):
        print("------------------------------")
        print("Visited:")
        for board in self.visited:
            print(board.raw_board())
        print("Unvisited")
        for board in self.unvisited:
            print(board.raw_board())
        print("------------------------------")
        print("")
        print("")
        print("")

#
# parent_board = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
#
# child_boards1 = [
# Board(2, 4, [0, 2, 3, 1, 5, 6, 7, 4], 3, parent_board),
# Board(2, 4, [4, 2, 3, 1, 0, 6, 7, 5], 2, parent_board),
# Board(2, 4, [4, 2, 0, 1, 5, 6, 7, 3], 3, parent_board),
# Board(2, 4, [4, 2, 3, 0, 5, 6, 7, 1], 1, parent_board),
# Board(2, 4, [4, 2, 3, 1, 5, 6, 0, 7], 1, parent_board),
# ]
#
# child_boards2 = [
# Board(2, 4, [4, 2, 0, 1, 5, 6, 3, 7], 1, child_boards1[4]),
# Board(2, 4, [4, 2, 3, 1, 5, 0, 6, 7], 1, child_boards1[4]),
# Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0], 1, child_boards1[4]),
# ]
#
# search = Search(parent_board)
# search.AddNewChildren(child_boards1)
# search.PrintLists()
# search.visit(Board(2, 4, [4, 2, 3, 1, 5, 6, 0, 7]))
# search.AddNewChildren(child_boards2)
# search.PrintLists()
# search.SortByMoveCost()
# search.PrintLists()
