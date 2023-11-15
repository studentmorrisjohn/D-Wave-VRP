# This example shows using SolutionPartitioningSolver with FullQuboSolver.
# It makes solving cvrp possible with using FullQuboSolver.

import sys
import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_dir, 'src'))

from vrp_solvers import SolutionPartitioningSolver, FullQuboSolver, AveragePartitionSolver
import DWaveSolvers
from input import *

if __name__ == '__main__':

    graph_path = os.path.join(project_dir, 'graphs/small.csv')

    # Parameters for solve function.
    only_one_const = 10000000.
    order_const = 1.

    for t in ['no_capacity']:
        print("Test : ", t)

        # Reading problem from file.
        path = os.path.join(project_dir, 'tests/my_inputs/' + t + '.test')
        problem = read_test(path, capacity = False)

        # Solving problem on SolutionPartitioningSolver.
        solver = AveragePartitionSolver(problem, limit_radius=20)
        solution = solver.solve(only_one_const, order_const, solver_type = 'cpu')

        # Checking if solution is correct.
        if solution == None or solution.check() == False:
            print("Solver hasn't find solution.\n")
            continue

        print("----------------")
        print("Solution : ", solution.solution) 
        print("Total cost : ", solution.total_cost())
        print("Weights : ", solution.all_weights())
        print("\n")
