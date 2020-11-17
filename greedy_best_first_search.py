import time

from board import Board, get_goal_1, get_goal_2
from heuristics import h0, h1, h2
from queue import PriorityQueue

from search_algorithm import SearchAlgorithmInterface


class GreedyBestSearch(SearchAlgorithmInterface):

    def __init__(self, heuristic_func=h0):
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_set = set()
        self.closed_list = []
        self.closed_set = set()
        self.heuristic_func = heuristic_func

    def solve(self, starting_board: Board) -> Board:
        print("Starting board state: ")
        print(starting_board)  # For debug
        current_board = starting_board
        current_board.parent = None
        self.open_queue.put((self.heuristic_func(current_board), time.time(), current_board))
        self.open_set.add(current_board)
        # if h(n) are equal, arbitrary selection instead of comparing
        # cost (here, we use time as that arbitrary comparator)

        goal_1 = get_goal_1(rows=starting_board.rows, columns=starting_board.columns)
        goal_2 = get_goal_2(rows=starting_board.rows, columns=starting_board.columns)

        while not (current_board.equals(goal_1) or current_board.equals(goal_2)):
            self.closed_list.insert(0, current_board)
            self.closed_set.add(current_board)

            children = current_board.get_successors()
            for child in children:
                if child in self.open_set:
                    continue  # We don't care to replace here, since we don't consider cost g(n), and h(n) is the same

                if child in self.closed_set:
                    continue  # Skip, since we've already explored, we don't consider cost g(n), and h(n) is the same

                self.open_queue.put((self.heuristic_func(child), time.time(), child))
                # again, if h(n) are equal, arbitrary selection instead of comparing
                # cost (here, we use time as that arbitrary comparator)
                self.open_set.add(child)

            if current_board not in self.open_set:
                continue  # ?????
            self.open_set.remove(current_board)
            current_board = self.open_queue.get()[2]

            while current_board in self.closed_set:  # Because of the initial board not being removed in open_queue....
                current_board = self.open_queue.get()[2]

        solved_board = current_board
        print("Solved board state: ")
        print(solved_board)

        print("Steps in reverse order")
        while current_board is not None:
            print(current_board)
            current_board = current_board.parent

        return solved_board


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

greedy_best_search_h0 = GreedyBestSearch()  # Default is h0
greedy_best_search_h1 = GreedyBestSearch(heuristic_func=h1)
greedy_best_search_h2 = GreedyBestSearch(heuristic_func=h2)

goal_state = greedy_best_search_h1.solve_timed(trial_board)
