from queue import PriorityQueue

import time

from Output.solution_output import SolutionOutput
from board import Board, get_goal_1, get_goal_2

from SearchAlgotrithms.search_algorithm import SearchAlgorithmInterface


class UniformCostSearch(SearchAlgorithmInterface):
    def __init__(self):
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_dict = dict()
        self.closed_list = []
        self.closed_set = set()

    def solve(self, starting_board: Board) -> any:
        start_time = time.time()

        current_board = starting_board
        current_board.parent = None
        self.open_queue.put((current_board.g, current_board))
        self.open_dict[current_board] = current_board.g

        goal_1 = get_goal_1(rows=starting_board.rows, columns=starting_board.columns)
        goal_2 = get_goal_2(rows=starting_board.rows, columns=starting_board.columns)

        while not (current_board.equals(goal_1) or current_board.equals(goal_2)):
            if (time.time() - start_time) > 60:
                return None

            current_board = self.search(current_board)

        return current_board

    def search(self, current_board):
        self.closed_list.insert(0, current_board)
        self.closed_set.add(current_board)
        children = current_board.get_successors()
        for child in children:
            if child in self.open_dict:
                if child.g < self.open_dict[child]:
                    # If successor s in OPEN with higher g(n), replace old version with new s
                    self.open_queue.put((child.g, child))
                    self.open_dict[child] = child.g
                    # NOTE_1 we can't replace in the priority queue,
                    # so instead we will end up adding it to the OPEN,
                    # priority will be sorted, and we will later add
                    # check to "delete" the remaining duplicate(s)
                continue

            if child in self.closed_set:
                # If successor s already in CLOSED, ignore s
                continue

            self.open_queue.put((child.g, child))
            self.open_dict[child] = child.g
        self.open_dict.pop(current_board, None)
        current_board = self.open_queue.get()[1]
        while current_board in self.closed_set:  # See NOTE_1 above for replacing OPEN nodes
            self.open_dict.pop(current_board, None)
            current_board = self.open_queue.get()[1]
        return current_board


# Boards to test out
initial_board1 = Board(initializing_input_data=[0, 2, 3, 4, 5, 6, 7, 1])
initial_board2 = Board(initializing_input_data=[4, 2, 3, 1, 5, 6, 7, 0])
initial_board3 = Board(initializing_input_data=[1, 0, 3, 7, 5, 2, 6, 4])
initial_board4 = Board(initializing_input_data=[3, 2, 5, 1, 6, 4, 7, 0])
initial_board5 = Board(initializing_input_data=[1, 2, 0, 3, 5, 6, 7, 4])
initial_board6 = Board(initializing_input_data=[1, 3, 5, 7, 2, 4, 6, 0])
initial_board7 = Board(initializing_input_data=[0, 3, 7, 5, 2, 6, 1, 4])
initial_board8 = Board(initializing_input_data=[1, 0, 3, 7, 5, 2, 6, 4])
initial_board9 = Board(rows=3, columns=3, initializing_input_data=[2, 5, 3, 4, 6, 0, 7, 8, 1])  # Breaks for now
trial_board = Board(initializing_input_data=[2, 0, 5, 3, 4, 7, 6, 1])

# uniform_cost_search = UniformCostSearch()
#
# # goal_state = uniform_cost_search.solve_timed(initial_board1)
# goal_state1 = uniform_cost_search.solve_timed(initial_board2)
# goal_state2 = uniform_cost_search.solve_timed(initial_board8)
# goal_state3 = uniform_cost_search.solve_timed(initial_board9)
#
# goals = [goal_state1, goal_state2, goal_state3]
#
# solution_output = SolutionOutput()
# solution_output.write_solutions("ucs_solutions.txt", goals)
# solution_output.write_search("ucs_search.txt", goals)
#
# print("----------------------")
# print("Completed Board-----------------")
# # goal_state.print_board()
