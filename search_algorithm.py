import time

from board import Board


class SearchAlgorithmInterface:
    def f(self, board: Board) -> int:
        return self.g(board) + self.h(board)

    def g(self, board: Board) -> int:
        pass

    def h(self, board: Board) -> int:
        pass

    def solve(self, board: Board) -> Board:
        pass

    def solve_timed(self, board: Board) -> Board:
        start = time.time()
        solved_board = self.solve(board)
        end = time.time()
        print("--Search time:-------------")
        print(end - start)
        return solved_board

