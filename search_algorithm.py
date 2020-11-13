import time

from board import Board


class SearchAlgorithmInterface:
    def solve(self, board: Board) -> Board:
        pass

    def solve_timed(self, board: Board) -> Board:
        start = time.time()
        solved_board = self.solve(board)
        end = time.time()
        print("--Search time:-------------")
        print(end - start)
        return solved_board

