from board import Board, get_goal_1, get_goal_2
from heuristics import h0, h1, h2
from queue import PriorityQueue

from search_algorithm import SearchAlgorithmInterface


class AStarSearch(SearchAlgorithmInterface):

    def __init__(self, heuristic_func=h0):
        self.open_queue: PriorityQueue = PriorityQueue()
        self.open_dict = dict()
        self.closed_list = []
        self.closed_dict = dict()
        self.heuristic_func = heuristic_func

    def solve(self, starting_board: Board) -> Board:
        print("Starting board state: ")
        print(starting_board)  # For debug
        current_board = starting_board
        current_board.parent = None
        h = self.heuristic_func(current_board)
        g = current_board.g
        f = g + h
        current_board.h = h
        current_board.f = f
        self.open_queue.put((f, current_board))
        self.open_dict[current_board] = (g, h)

        goal_1 = get_goal_1(rows=starting_board.rows, columns=starting_board.columns)
        goal_2 = get_goal_2(rows=starting_board.rows, columns=starting_board.columns)

        while not (current_board.equals(goal_1) or current_board.equals(goal_2)):
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
                        child.f = f
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
                        child.f = f
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

            self.open_dict.pop(current_board, None)
            current_board = self.open_queue.get()[1]

            while current_board in self.closed_dict:  # See NOTE_1 above for replacing OPEN nodes
                self.open_dict.pop(current_board, None)
                current_board = self.open_queue.get()[1]

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

a_star_search_h0 = AStarSearch()  # Default is h0
a_star_search_h1 = AStarSearch(heuristic_func=h1)
a_star_search_h2 = AStarSearch(heuristic_func=h2)

goal_state = a_star_search_h1.solve_timed(trial_board)
