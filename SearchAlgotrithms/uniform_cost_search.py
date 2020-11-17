from queue import PriorityQueue

import time

from Output.solution_output import SolutionOutput
from board import Board, get_goal_1, get_goal_2

from SearchAlgotrithms.search_algorithm import SearchAlgorithmInterface


class UniformCostSearch(SearchAlgorithmInterface):
    def __init__(self, time_out=60):
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_dict = dict()
        self.closed_list = []
        self.closed_set = set()
        self.time_out = time_out

    def solve(self, starting_board: Board) -> any:
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_dict = dict()
        self.closed_list = []
        self.closed_set = set()
        start_time = time.time()

        current_board = starting_board
        current_board.parent = None
        self.open_queue.put((current_board.g, current_board))
        self.open_dict[current_board] = current_board.g

        goal_1 = get_goal_1(rows=starting_board.rows, columns=starting_board.columns)
        goal_2 = get_goal_2(rows=starting_board.rows, columns=starting_board.columns)

        while not (current_board.equals(goal_1) or current_board.equals(goal_2)):
            if (time.time() - start_time) > self.time_out:
                return None

            current_board = self.search(current_board)
            if current_board is None:
                return None

        current_board.open_length_solved = len(self.open_dict)
        current_board.closed_length_solved = len(self.closed_list)
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

        if len(self.open_dict) != 0:
            self.open_dict.pop(current_board, None)
            current_board = self.open_queue.get()[1]
        else:
            print("UCS True No Solution!")
            return None

        while current_board in self.closed_set:  # See NOTE_1 above for replacing OPEN nodes
            if len(self.open_dict) != 0:
                self.open_dict.pop(current_board, None)
                current_board = self.open_queue.get()[1]
            else:
                print("UCS True No Solution!")
                return None

        return current_board
