"""

"""
import sys
import argparse
import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver.routing_enums_pb2 import FirstSolutionStrategy, LocalSearchMetaheuristic

from metrics import overlap_distance
from utils import is_superstring

# Distance callback
def create_distance_callback(dist_matrix):
    # Create a callback to calculate distances between cities.

    def distance_callback(from_node, to_node):
        return int(dist_matrix[from_node][to_node])

    return distance_callback


def build_superpermutation(routing, assignment, permutations, dist_matrix):
    # Display the solution.
    # Only one route
    route_number = 0
    index = routing.Start(route_number) # Index of the variable for the starting node.
    next_index = assignment.Value(routing.NextVar(index))

    superpermutation = permutations[routing.IndexToNode(index)]

    while not routing.IsEnd(next_index):
        # Convert variable indices to node indices and build 
        # the superpermutation.
        # get node values (indices to permutations)
        curr_node = routing.IndexToNode(index)
        next_node = routing.IndexToNode(next_index)
        # append the necessary suffix of the next permutation to the superpermutation
        superpermutation += permutations[next_node][-dist_matrix[curr_node, next_node]:]
        # get next indices
        index = assignment.Value(routing.NextVar(index))
        next_index = assignment.Value(routing.NextVar(index))
    
    return superpermutation

    
def run_tsp_search(permutations, dist_matrix, 
                   start_node, strategy, heuristic, time_limit):
    # number of "cities" in the traveling salesman problem
    tsp_size = len(permutations)
    # should only find one route
    num_routes = 1

    # Create routing model
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, num_routes, start_node)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        
        first_solution_strategy = getattr(FirstSolutionStrategy, strategy)
        local_search_metaheuristic = getattr(LocalSearchMetaheuristic, heuristic)

        search_parameters.first_solution_strategy = first_solution_strategy
        search_parameters.local_search_metaheuristic = local_search_metaheuristic
        search_parameters.time_limit_ms = time_limit

        # Create the distance callback.
        dist_callback = create_distance_callback(dist_matrix)
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        # if solution was found show it
        if assignment:
            superpermutation = build_superpermutation(routing, assignment, 
                                                      permutations, dist_matrix)

            print('\nSuperpermutation:', superpermutation, sep='\n')
            print('\nSuperpermutation length:', len(superpermutation), sep='\n')   
            print('\nIs superpermutation:', is_superstring(permutations, superpermutation))

        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')


def main():
    parser = argparse.ArgumentParser(description="Search for superpermutations")
    
    # file to read distance matrix from
    parser.add_argument('file_path', type=str, 
                        help='path to file containing distance matrix')
    # permutation to start from
    parser.add_argument('-s', '--start', type=str, default=0,
                        help='start node in traveling salesman problem')

    parser.add_argument('--strategy', type=str, default='AUTOMATIC',
        choices=['AUTOMATIC', 'PATH_CHEAPEST_ARC', 'PATH_MOST_CONSTRAINED_ARC',
                 'EVALUATOR_STRATEGY', 'SAVINGS', 'SWEEP', 'CHRISTOFIDES',
                 'ALL_UNPERFORMED', 'BEST_INSERTION', 'PARALLEL_CHEAPEST_INSERTION',
                 'LOCAL_CHEAPEST_INSERTION', 'GLOBAL_CHEAPEST_ARC', 'LOCAL_CHEAPEST_ARC',
                 'FIRST_UNBOUND_MIN_VALUE'],
        help='First solution strategy, used as starting point of local search.')

    parser.add_argument('--heuristic', type=str, default='AUTOMATIC',
        choices=['AUTOMATIC', 'GREEDY_DESCENT' , 'GUIDED_LOCAL_SEARCH',	
                 'SIMULATED_ANNEALING', 'TABU_SEARCH', 'OBJECTIVE_TABU_SEARCH'],
        help='Metaheuristics for local search strategies.')

    parser.add_argument('--time_limit', type=int, default=sys.maxsize, 
        help='Limit in milliseconds to the time spent in the search.')

    
    args = parser.parse_args()

    data = np.load(args.file_path)
    # Permutations
    permutations = data['permutations']
    # Distance matrix
    dist_matrix = data['distance_matrix']

    run_tsp_search(permutations, dist_matrix, 
                   args.start, args.strategy, 
                   args.heuristic, args.time_limit)
    

if __name__ == '__main__':
    main()
