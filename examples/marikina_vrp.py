# This example shows using SolutionPartitioningSolver with FullQuboSolver.
# It makes solving cvrp possible with using FullQuboSolver.

import sys
import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_dir, 'src'))

from vrp_solvers import SolutionPartitioningSolver, FullQuboSolver, DBScanSolver
import DWaveSolvers
from input import *

if __name__ == '__main__':

    graph_path = os.path.join(project_dir, 'graphs/small.csv')

    # Parameters for solve function.
    only_one_const = 10000000.
    order_const = 1.

    solutions = []

    for i in range(100):

        for t in ['marikina']:
            print("Test : ", t)

            # Reading problem from file.
            path = os.path.join(project_dir, 'tests/my_inputs/' + t + '.test')
            problem = read_test(path)

            print("Testing Using CPU")

            # # Solving problem on SolutionPartitioningSolver.
            solver = SolutionPartitioningSolver(problem, FullQuboSolver(problem), random = 100)
            solution = solver.solve(only_one_const, order_const, solver_type = 'cpu')

            print("Full QUBO SPS: ")

            # Checking if solution is correct.
            if solution == None or solution.check() == False:
                print("Solver hasn't find solution.\n")
                continue

            print("Solution : ", solution.solution) 
            print("Total cost : ", solution.total_cost())
            print("Weights : ", solution.all_weights())
            print("\n")

            solutions.append(solution)

            print("Testing Using QPU")

            # # Solving problem on SolutionPartitioningSolver.
            solver = SolutionPartitioningSolver(problem, FullQuboSolver(problem), random = 100)
            solution = solver.solve(only_one_const, order_const, solver_type = 'qpu')

            print("Full QUBO SPS: ")

            # Checking if solution is correct.
            if solution == None or solution.check() == False:
                print("Solver hasn't find solution.\n")
                continue

            print("Solution : ", solution.solution) 
            print("Total cost : ", solution.total_cost())
            print("Weights : ", solution.all_weights())
            print("\n")

            solutions.append(solution)
