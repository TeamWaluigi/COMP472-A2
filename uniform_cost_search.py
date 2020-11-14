from board import Board, get_goal_1, get_goal_2
from search import Search

from search_algorithm import SearchAlgorithmInterface


class UniformCostSearch(SearchAlgorithmInterface):
    def solve(self, board):
        current_board = board
        # current_board.print_board()  # For debug

        goal_1 = get_goal_1(rows=board.rows, columns=board.columns)
        goal_2 = get_goal_2(rows=board.rows, columns=board.columns)
        # goal_1.print_board()  # For debug
        # goal_2.print_board()  # For debug

        search = Search(board)

        while not current_board.equals(goal_1) and not current_board.equals(goal_2):
            children = current_board.get_successors()
            search.add_new_children(children)
            if len(search.unvisited) > 0:
                current_board = search.unvisited.pop(0)
                search.visited.append(current_board)
        print(search.unvisited.__len__())
        print(search.visited.__len__())
        return current_board


# Boards to test out
initial_board = Board([4, 2, 3, 1, 5, 6, 7, 0])
initial_board2 = Board([4, 2, 3, 1, 5, 6, 7, 0])
initial_board3 = Board([1, 0, 3, 7, 5, 2, 6, 4])
initial_board4 = Board([3, 2, 5, 1, 6, 4, 7, 0])
initial_board5 = Board([1, 2, 0, 3, 5, 6, 7, 4])
initial_board6 = Board([1, 3, 5, 7, 2, 4, 6, 0])
initial_board7 = Board([0, 3, 7, 5, 2, 6, 1, 4])
initial_board8 = Board([1, 0, 3, 7, 5, 2, 6, 4])
initial_board9 = Board(rows=3, columns=3, raw_board=[2, 5, 3, 4, 6, 0, 7, 8, 1])  # Breaks for now

uniform_cost_search = UniformCostSearch()

goal_state = uniform_cost_search.solve_timed(initial_board9)
print("----------------------")
print("Completed Board-----------------")
goal_state.print_board()

