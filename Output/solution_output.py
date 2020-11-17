import decimal
import os


class SolutionOutput:

    def __init__(self, count=0):
        self.count = count
        self.no_solutions = 0
        self.search_length = []

    def write_solutions(self, file_name, puzzles):
        self.count = 0
        for i in range(len(puzzles)):
            unique_name = str(self.count) + "_" + file_name
            file_path = "../Output/SolutionFiles/" + unique_name
            if os.path.exists(file_path):
                os.remove(file_path)
            f = open(file_path, "x")
            f = open(file_path, "a")

            if puzzles[i] is None:
                f.write("No Solution")
                self.no_solutions += 1
                continue

            nodes, costs = self.find_path(puzzles[i])
            self.search_length = len(nodes)

            decimal.getcontext().rounding = decimal.ROUND_DOWN
            total_time = decimal.Decimal(puzzles[i].execution_time)
            for node_count in range(len(nodes)):
                current_board = nodes[node_count].tiles_to_flat_list()
                zero_position = 0
                row = ""
                for j in range(len(current_board)):
                    if current_board[j] == 0:
                        zero_position = j
                row = str(zero_position) + " " + str(costs[node_count]) + " "
                for j in range(len(current_board)):
                    row = row + str(current_board[j]) + " "
                row = row + "\n"
                f.write(row)
            f.write(str(puzzles[i].g) + " " + str(round(total_time, 2)))
            f.close()
            self.count += 1

    def write_search(self, file_name, puzzles):
        self.count = 0
        for i in range(len(puzzles)):
            unique_name = str(self.count) + "_" + file_name
            file_path = "../Output/SearchFiles/" + unique_name
            if os.path.exists(file_path):
                os.remove(file_path)
            file = open(file_path, "x")
            file = open(file_path, "a")

            if puzzles[i] is None:
                file.write("No Solution")
                continue
            nodes, costs = self.find_path(puzzles[i])
            decimal.getcontext().rounding = decimal.ROUND_DOWN
            f, h = puzzles[i].f, puzzles[i].h
            for node_count in range(len(nodes)):
                current_board = nodes[node_count].tiles_to_flat_list()
                row = str(f) + " " + str(costs[node_count]) + " " + str(h) + " "
                for j in range(len(current_board)):
                    row = row + str(current_board[j]) + " "
                row = row + "\n"
                file.write(row)
            file.close()
            self.count += 1

    def find_path(self, board):
        nodes = []
        costs = []
        nodes.append(board)
        while board.parent is not None:
            costs.append(board.g - board.parent.g)
            nodes.append(board.parent)
            board = board.parent
        costs.append(0)
        costs.reverse()
        nodes.reverse()
        return nodes, costs

    def analysis(self):
        average_search = 0
        sum_search = 0
        for i in range(len(self.search_length)):
            sum_search += self.search_length[i]
