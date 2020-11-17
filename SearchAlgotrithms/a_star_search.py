from board import Board, get_goal_1, get_goal_2
from SearchAlgotrithms.heuristics import h0, h1, h2
from queue import PriorityQueue
import time

from SearchAlgotrithms.search_algorithm import SearchAlgorithmInterface


class AStarSearch(SearchAlgorithmInterface):

    def __init__(self, heuristic_func=h0):
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_dict = dict()
        self.closed_list = []
        self.closed_dict = dict()
        self.heuristic_func = heuristic_func

    def solve(self, starting_board: Board) -> any:
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_dict = dict()
        self.closed_list = []
        self.closed_dict = dict()
        start_time = time.time()

        current_board = starting_board
        current_board.parent = None
        h = self.heuristic_func(current_board)
        g = current_board.g
        current_f = g + h
        current_board.h = h
        current_board.f = current_f
        self.open_queue.put((current_f, current_board))
        self.open_dict[current_board] = (g, h)

        goal_1 = get_goal_1(rows=starting_board.rows, columns=starting_board.columns)
        goal_2 = get_goal_2(rows=starting_board.rows, columns=starting_board.columns)

        while not (current_board.equals(goal_1) or current_board.equals(goal_2)):
            if (time.time() - start_time) > 60:
                return None

            current_board = self.search(current_board)
            if current_board is None:
                return None

        return current_board

    def search(self, current_board):
        self.closed_list.insert(0, current_board)
        self.closed_dict[current_board] = (current_board.g, current_board.h)

        children = current_board.get_successors()
        for child in children:
            if child in self.open_dict:
                if child.g < self.open_dict[child][0]:
                    # If successor s in OPEN with higher f(n), replace old version with new s
                    # We only need to compare g(n) here, since h(n) remains the same!
                    new_g = child.g
                    h = self.open_dict[child][1]
                    new_f = new_g + h
                    child.h = h
                    child.f = new_f
                    self.open_queue.put((new_f, child))
                    self.open_dict[child] = (new_g, h)
                    # NOTE_1 we can't replace in the priority queue,
                    # so instead we will end up adding it to the OPEN,
                    # priority will be sorted, and we will later add
                    # check to "delete" the remaining duplicate(s)
                continue

            if child in self.closed_dict:
                if child.g < self.closed_dict[child][0]:
                    # If successor s already in CLOSED with higher f(n), replace old version with new s
                    # We only need to compare g(n) here, since h(n) remains the same!
                    new_g = child.g
                    h = self.closed_dict[child][1]
                    new_f = new_g + h
                    child.h = h
                    child.f = new_f
                    self.closed_dict.pop(child)
                    self.closed_list.remove(child)
                    self.open_queue.put((new_f, child))
                    self.open_dict[child] = (new_g, h)
                    # NOTE_1 we can't replace in the priority queue,
                    # so instead we will end up adding it to the OPEN,
                    # priority will be sorted, and we will later add
                    # check to "delete" the remaining duplicate(s)
                continue

            g = child.g
            h = self.heuristic_func(child)
            f = g + h
            child.h = h
            child.f = f
            self.open_queue.put((f, child))
            self.open_dict[child] = (g, h)

        if len(self.open_dict) != 0:
            self.open_dict.pop(current_board, None)
            current_board = self.open_queue.get()[1]
        else:
            print("ASS True No Solution!")
            return None

        while current_board in self.closed_dict:  # See NOTE_1 above for replacing OPEN nodes
            if len(self.open_dict) != 0:
                self.open_dict.pop(current_board, None)
                current_board = self.open_queue.get()[1]
            else:
                print("ASS True No Solution!")
                return None

        return current_board
