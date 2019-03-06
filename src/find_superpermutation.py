import sys
import numpy as np
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

from metrics import permutation_distance

def check_superpermutation(permutations, superpermutation):
    return all(p in superpermutation for p in permutations)

# Distance callback
def create_distance_callback(dist_matrix):
    # Create a callback to calculate distances between cities.

    def distance_callback(from_node, to_node):
        return int(dist_matrix[from_node][to_node])

    return distance_callback

def main():
    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        start = int(sys.argv[2])
    else:
        raise RuntimeError("Must provide the number of symbols as an argument")

    data = np.load(file_path)
    # Permutations
    permutations = data['permutations']
    # Distance matrix
    dist_matrix = data['distance_matrix']

    # number of "cities" in the traveling salesman problem
    tsp_size = len(permutations)
    # should only find one route
    num_routes = 1
    # permutation to start from
    #start = 22

    # Create routing model
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, num_routes, start)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        # Create the distance callback.
        dist_callback = create_distance_callback(dist_matrix)
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        # if solution was found show it
        if assignment:
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

            print('\nSuperpermutation:', superpermutation, sep='\n')
            print('\nSuperpermutation length:', len(superpermutation), sep='\n')   
            print('\nIs superpermutation:', check_superpermutation(permutations, superpermutation))
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')

if __name__ == '__main__':
    main()
