from board import Board, get_goal_1, get_goal_2
from heuristics import h1
from queue import PriorityQueue

from search_algorithm import SearchAlgorithmInterface


class GreedyBestSearch(SearchAlgorithmInterface):

    def __init__(self, heuristic_func=h1):
        self.open = PriorityQueue()
        self.closed = []
        self.heuristic_func = heuristic_func

    def solve(self, starting_board: Board) -> Board:
        print("Starting board state: ")
        print(starting_board)  # For debug
        current_board = starting_board
        current_board.parent = None
        self.open.put((0, current_board))

        goal_1 = get_goal_1(rows=starting_board.rows, columns=starting_board.columns)
        goal_2 = get_goal_2(rows=starting_board.rows, columns=starting_board.columns)

        while not (current_board.equals(goal_1) or current_board.equals(goal_2)):
            self.closed.insert(0, current_board)

            children = current_board.get_successors()
            for child in children:
                if child in self.closed:
                    continue  # TODO this should be changed, right?
                if any(child.equals(node[1]) for node in self.open.queue):
                    continue  # TODO this should be changed, right?
                self.open.put((self.heuristic_func(child), child))

            current_board = self.open.get()[1]

        solved_board = current_board
        print("Solved board state: ")
        print(solved_board)

        print("Steps in reverse order")
        while current_board is not None:
            print(current_board)
            current_board = current_board.parent

        return solved_board


# Boards to test out
initial_board = Board([4, 2, 3, 1, 5, 6, 7, 0])
initial_board2 = Board([4, 2, 3, 1, 5, 6, 7, 0])
initial_board3 = Board([1, 0, 3, 7, 5, 2, 6, 4])
initial_board4 = Board([3, 2, 5, 1, 6, 4, 7, 0])
initial_board5 = Board([1, 2, 0, 3, 5, 6, 7, 4])
initial_board6 = Board([1, 3, 5, 7, 2, 4, 6, 0])
initial_board7 = Board([0, 3, 7, 5, 2, 6, 1, 4])
initial_board8 = Board([3, 0, 1, 4, 2, 6, 5, 7])
initial_board9 = Board(rows=3, columns=3, raw_board=[2, 5, 3, 4, 6, 0, 7, 8, 1])
initial_board10 = Board(rows=3, columns=3, raw_board=[2, 0, 7, 4, 6, 5, 8, 3, 1])

greedy_best_search = GreedyBestSearch()

goal_state = greedy_best_search.solve_timed(initial_board8)
