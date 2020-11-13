from board import Board
from search import Search

from search_algorithm import SearchAlgorithmInterface


class UniformCostSearch(SearchAlgorithmInterface):
    def solve(self, board):
        current_view = board
        current_view.print_board()
        search = Search(board)
        while not current_view.is_goal(2, 4, goal1) and not current_view.is_goal(2, 4, goal2):
            children = current_view.calculate_successors()
            search.add_new_children(children)
            if len(search.unvisited) > 0:
                current_view = search.unvisited.pop(0)
                search.visited.append(current_view)
        print(search.unvisited.__len__())
        print(search.visited.__len__())
        return current_view


parent_board = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
parent_board2 = Board(2, 4, [4, 2, 3, 1, 5, 6, 7, 0])
parent_board3 = Board(2, 4, [1, 0, 3, 7, 5, 2, 6, 4])
parent_board4 = Board(2, 4, [3, 2, 5, 1, 6, 4, 7, 0])
parent_board5 = Board(2, 4, [1, 2, 0, 3, 5, 6, 7, 4])
parent_board6 = Board(2, 4, [1, 3, 5, 7, 2, 4, 6, 0])
parent_board7 = Board(2, 4, [0, 3, 7, 5, 2, 6, 1, 4])
parent_board8 = Board(2, 4, [1, 0, 3, 7, 5, 2, 6, 4])

goal1 = [1, 2, 3, 4, 5, 6, 7, 0]
goal2 = [1, 3, 5, 7, 2, 4, 6, 0]

uniform_cost_search = UniformCostSearch()

goal_state = uniform_cost_search.solve_timed(parent_board)
print("----------------------")
print("----------------------")
goal_state.print_board()

