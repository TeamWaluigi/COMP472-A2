import time

from board import Board, get_goal_1, get_goal_2
from SearchAlgotrithms.heuristics import h0, h1, h2
from queue import PriorityQueue

from SearchAlgotrithms.search_algorithm import SearchAlgorithmInterface


class GreedyBestSearch(SearchAlgorithmInterface):

    def __init__(self, heuristic_func=h0, time_out=60):
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_set = set()
        self.closed_list = []
        self.closed_set = set()
        self.heuristic_func = heuristic_func
        self.time_out = time_out

    def solve(self, starting_board: Board) -> any:
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_set = set()
        self.closed_list = []
        self.closed_set = set()
        start_time = time.time()

        current_board = starting_board
        current_board.parent = None
        h = self.heuristic_func(current_board)
        current_board.h = h
        self.open_queue.put((h, time.time(), current_board))
        self.open_set.add(current_board)
        # if h(n) are equal, arbitrary selection instead of comparing
        # cost (here, we use time as that arbitrary comparator)

        goal_1 = get_goal_1(rows=starting_board.rows, columns=starting_board.columns)
        goal_2 = get_goal_2(rows=starting_board.rows, columns=starting_board.columns)

        while not (current_board.equals(goal_1) or current_board.equals(goal_2)):
            if (time.time() - start_time) > self.time_out:
                return None

            current_board = self.search(current_board)
            if current_board is None:
                return None

        current_board.open_length_solved = len(self.open_set)
        current_board.closed_length_solved = len(self.closed_list)
        return current_board

    def search(self, current_board):
        self.closed_list.insert(0, current_board)
        self.closed_set.add(current_board)

        children = current_board.get_successors()
        for child in children:
            if child in self.open_set:
                continue  # We don't care to replace here, since we don't consider cost g(n), and h(n) is the same

            if child in self.closed_set:
                continue  # Skip, since we've already explored, we don't consider cost g(n), and h(n) is the same

            h = self.heuristic_func(child)
            child.h = h
            self.open_queue.put((h, time.time(), child))
            # again, if h(n) are equal, arbitrary selection instead of comparing
            # cost (here, we use time as that arbitrary comparator)
            self.open_set.add(child)

        if len(self.open_set) != 0:
            self.open_set.remove(current_board)
            current_board = self.open_queue.get()[2]
        else:
            print("GBS True No Solution!")
            return None

        while current_board in self.closed_set:  # See NOTE_1 above for replacing OPEN nodes
            if len(self.open_set) != 0:
                current_board = self.open_queue.get()[2]
            else:
                print("while GBS True No Solution!")
                return None

        return current_board
