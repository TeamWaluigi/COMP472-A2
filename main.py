import sys

from Input.puzzle_generator import generate_puzzles
from Input.puzzle_reader import get_puzzles_from_file
from Output.solution_output import SolutionOutput
from SearchAlgotrithms.a_star_search import AStarSearch
from SearchAlgotrithms.greedy_best_first_search import GreedyBestSearch
from SearchAlgotrithms.heuristics import h1, h2
from SearchAlgotrithms.uniform_cost_search import UniformCostSearch
from board import Board

puzzle_file_path = "Input\Puzzles\Puzzles.txt"
puzzle_rows = 2
puzzle_columns = 4
total_puzzles = 50  # TODO set to 50
time_out_value = 60.0
# time_out_value = sys.float_info.max

# Generate puzzles (If needed)
generate_puzzles(row=puzzle_rows, column=puzzle_columns, count=total_puzzles)

# Read puzzles from Input file
puzzles = get_puzzles_from_file(puzzle_file_path=puzzle_file_path)

# Set up Search Algorithms
search_algorithms = dict()
# UniformCostSearch
uniform_cost_search = UniformCostSearch(time_out=time_out_value)
search_algorithms["uniform_cost_search"] = [uniform_cost_search, []]
# GreedyBestSearch
greedy_best_search_h0 = GreedyBestSearch(time_out=time_out_value)  # Default is h0
search_algorithms["greedy_best_search_h0"] = [greedy_best_search_h0, []]
greedy_best_search_h1 = GreedyBestSearch(heuristic_func=h1, time_out=time_out_value)
search_algorithms["greedy_best_search_h1"] = [greedy_best_search_h1, []]
greedy_best_search_h2 = GreedyBestSearch(heuristic_func=h2, time_out=time_out_value)
search_algorithms["greedy_best_search_h2"] = [greedy_best_search_h2, []]
# AStarSearch
a_star_search_h0 = AStarSearch(time_out=time_out_value)  # Default is h0
search_algorithms["a_star_search_h0"] = [a_star_search_h0, []]
a_star_search_h1 = AStarSearch(heuristic_func=h1, time_out=time_out_value)
search_algorithms["a_star_search_h1"] = [a_star_search_h1, []]
a_star_search_h2 = AStarSearch(heuristic_func=h2, time_out=time_out_value)
search_algorithms["a_star_search_h2"] = [a_star_search_h2, []]


# Solve each puzzle
for puzzle in puzzles:
    print("Starting puzzle: " + str(puzzle))
    for search_algorithm in search_algorithms:
        print("Evaluated by: " + search_algorithm)
        puzzle_board = Board(rows=puzzle_rows, columns=puzzle_columns, initializing_input_data=puzzle)
        solution = search_algorithms[search_algorithm][0].solve_timed(puzzle_board)
        search_algorithms[search_algorithm][1].append(solution)

print("woah!")

print("Starting Output")
solution_output = SolutionOutput()
solution_output.write_solutions("ucs_solution.txt", search_algorithms["uniform_cost_search"][1])
solution_output.write_solutions("gbfs-h1_solution.txt", search_algorithms["greedy_best_search_h1"][1])
solution_output.write_solutions("gbfs-h2_solution.txt", search_algorithms["greedy_best_search_h2"][1])
solution_output.write_solutions("astar-h1_solution.txt", search_algorithms["a_star_search_h1"][1])
solution_output.write_solutions("astar-h2_solution.txt", search_algorithms["a_star_search_h2"][1])

solution_output.write_search("ucs_search.txt", search_algorithms["uniform_cost_search"][1])
solution_output.write_search("gbfs-h1_search.txt", search_algorithms["greedy_best_search_h1"][1])
solution_output.write_search("gbfs-h2_search.txt", search_algorithms["greedy_best_search_h2"][1])
solution_output.write_search("astar-h1_search.txt", search_algorithms["a_star_search_h1"][1])
solution_output.write_search("astar-h2_search.txt", search_algorithms["a_star_search_h2"][1])

# TODO
# Print Output
for puzzle in puzzles:
    for search_algorithm in search_algorithms:
        # TODO following is an example, switch this whole thing as needed
        print(search_algorithm + ": performance")
        for solution in search_algorithms[search_algorithm][1]:
            print(solution)
