import time

from board import Board


class SearchAlgorithmInterface:
    def f(self, board: Board) -> int:
        return self.g(board) + self.h(board)

    def g(self, board: Board) -> int:
        pass

    def h(self, board: Board) -> int:
        pass

    def solve(self, board: Board) -> any:
        pass

    def solve_timed(self, board: Board) -> any:
        start = time.time()
        solved_board = self.solve(board)
        end = time.time()
        print("--Search time:-------------")
        execution_time = end - start
        print(execution_time)
        solved_board.execution_time = execution_time
        return solved_board

