from Input.puzzle_generator import generate_puzzles
from Input.puzzle_reader import get_puzzles_from_file
from Output.solution_output import SolutionOutput
from SearchAlgotrithms.a_star_search import AStarSearch
from SearchAlgotrithms.greedy_best_first_search import GreedyBestSearch
from SearchAlgotrithms.heuristics import h1, h2
from SearchAlgotrithms.uniform_cost_search import UniformCostSearch
from board import Board

puzzle_file_path = "Input\Puzzles\Puzzles.txt"

# Generate puzzles (If needed)
generate_puzzles(2, 4, 5)  # Comment out as needed  # TODO increase to 50

# Read puzzles from Input file
puzzles = get_puzzles_from_file(puzzle_file_path=puzzle_file_path)

# Set up Search Algorithms
search_algorithms = dict()
# UniformCostSearch
uniform_cost_search = UniformCostSearch()
search_algorithms["uniform_cost_search"] = [uniform_cost_search, []]
# GreedyBestSearch
greedy_best_search_h0 = GreedyBestSearch()  # Default is h0
search_algorithms["greedy_best_search_h0"] = [greedy_best_search_h0, []]
greedy_best_search_h1 = GreedyBestSearch(heuristic_func=h1)
search_algorithms["greedy_best_search_h1"] = [greedy_best_search_h1, []]
greedy_best_search_h2 = GreedyBestSearch(heuristic_func=h2)
search_algorithms["greedy_best_search_h2"] = [greedy_best_search_h2, []]
# AStarSearch
a_star_search_h0 = AStarSearch()  # Default is h0
search_algorithms["a_star_search_h0"] = [a_star_search_h0, []]
a_star_search_h1 = AStarSearch(heuristic_func=h1)
search_algorithms["a_star_search_h1"] = [a_star_search_h1, []]
a_star_search_h2 = AStarSearch(heuristic_func=h2)
search_algorithms["a_star_search_h2"] = [a_star_search_h2, []]


# Solve each puzzle
for puzzle in puzzles:
    print(puzzle)
    for search_algorithm in search_algorithms:
        puzzle_board = Board(initializing_input_data=puzzle)
        solution = search_algorithms[search_algorithm][0].solve(puzzle_board)
        search_algorithms[search_algorithm][1].append(solution)

print("woah!")

print("Starting Output")
solution_output = SolutionOutput()
solution_output.write_solutions("ucs_solution.txt", search_algorithms["uniform_cost_search"][1])
solution_output.write_solutions("gbfs-h1_solution.txt", search_algorithms["greedy_best_search_h1"][1])
solution_output.write_solutions("gbfs-h2_solution.txt", search_algorithms["greedy_best_search_h2"][1])
solution_output.write_solutions("astar-h1_solution", search_algorithms["a_star_search_h1"][1])
solution_output.write_solutions("astar-h2_solution", search_algorithms["a_star_search_h2"][1])

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
