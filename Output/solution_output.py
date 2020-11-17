import decimal
import os


class SolutionOutput:

    def __init__(self, count=0):
        self.count = count
        self.no_solutions = 0
        self.search_length = []
        self.total_puzzles = 0
        self.costs = []
        self.execution_times = []
        self.closed_size = []
        self.optimal_cost = 0.1

    def write_solutions(self, file_name, puzzles):
        self.count = 0
        self.no_solutions = 0
        self.search_length = []
        self.costs = []
        self.execution_times = []
        self.closed_size = []
        self.total_puzzles = len(puzzles)

        for i in range(len(puzzles)):
            unique_name = str(self.count) + "_" + file_name
            file_path = "Output/SolutionFiles/" + unique_name
            if os.path.exists(file_path):
                os.remove(file_path)
            f = open(file_path, "x")
            f = open(file_path, "a")

            if puzzles[i] is None:
                f.write("No Solution")
                self.no_solutions += 1
                continue

            nodes, costs = self.find_path(puzzles[i])
            self.search_length.append(len(nodes))
            self.execution_times.append(puzzles[i].execution_time)
            decimal.getcontext().rounding = decimal.ROUND_DOWN
            total_time = decimal.Decimal(puzzles[i].execution_time)
            self.closed_size.append(puzzles[i].closed_length_solved)
            for node_count in range(len(nodes)):
                current_board = nodes[node_count].tiles_to_flat_list()
                zero_position = 0
                row = ""
                for j in range(len(current_board)):
                    if current_board[j] == 0:
                        zero_position = j
                row = str(nodes[node_count].last_tile_moved) + " " + str(costs[node_count]) + " "
                for j in range(len(current_board)):
                    row = row + str(current_board[j]) + " "
                row = row + "\n"
                f.write(row)
            f.write(str(puzzles[i].g) + " " + str(round(total_time, 2)))
            self.costs.append(puzzles[i].g)
            f.close()
            self.count += 1
        self.analysis(file_name)

    def write_search(self, file_name, puzzles):
        self.count = 0
        for i in range(len(puzzles)):
            unique_name = str(self.count) + "_" + file_name
            file_path = "Output/SearchFiles/" + unique_name
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

    def analysis(self, unique_name):
        total_visited = 0
        for size in self.closed_size:
            total_visited += size
        average_visited = total_visited / self.total_puzzles
        sum_search = 0
        for search in self.search_length:
            sum_search += search
        average_search = sum_search/self.total_puzzles
        total_no_solutions = self.no_solutions
        average_no_solutions = self.no_solutions / self.total_puzzles
        total_cost = 0.0
        for cost in self.costs:
            total_cost += cost
        average_cost = total_cost / self.total_puzzles
        total_execution_time = 0.0
        for time in self.execution_times:
            total_execution_time += time
        average_execution_time = time / len(self.execution_times)

        if "ucs" in unique_name :
            self.optimal_cost = total_cost

        file_path = "Output/Analysis/" + unique_name
        if os.path.exists(file_path):
            os.remove(file_path)
        file = open(file_path, "x")
        file = open(file_path, "a")
        file.write("Total Solution Path Size : " + str(total_visited) + "\n")
        file.write("Average Solution Path Size : " + str(average_visited) + "\n")
        file.write("Total Puzzles : " + str(self.total_puzzles) + "\n")
        file.write("Average Length of Search : " + str(average_search) + "\n")
        file.write("Total Length of Search : " + str(sum_search) + "\n")
        file.write("Average Number of No Solutions : " + str(average_no_solutions) + "\n")
        file.write("Total Number of No Solutions : " + str(total_no_solutions) + "\n")
        file.write("Total Cost : " + str(total_cost) + "\n")
        file.write("Average Cost : " + str(average_cost) + "\n")
        file.write("Total Execution Time : " + str(total_execution_time) + "\n")
        file.write("Average Execution Time : " + str(average_execution_time) + "\n")
        file.write("Optimal Solution Cost : " + str(self.optimal_cost) + "\n")
        file.write("Optimality : " + str(total_cost / self.optimal_cost))


