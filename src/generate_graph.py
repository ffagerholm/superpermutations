import sys
import csv
from itertools import permutations, combinations
import numpy as np
from metrics import overlap_distance



def generate_permutation_graph(n_symbols, file_path):
    """
    """
    symbols = map(str, range(1, n_symbols + 1))
    perms = permutations(symbols)

    # write graph to a csv-file as an edgelist
    with open(file_path, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        for perm1, perm2 in combinations(perms, 2):
            weight1 = overlap_distance(perm1, perm2)
            p1 = ''.join(perm1)
            p2 = ''.join(perm2)
            w1 = "{{'weight': {:.2f} }}".format(weight1)
            # add forward edge
            writer.writerow([p1, p2, w1])
            
            weight2 = overlap_distance(perm2, perm1)
            w2 = "{{'weight': {:.2f} }}".format(weight2)
            # add backward edge
            writer.writerow([p2, p1, w2])            


def main():
    if len(sys.argv) == 3:
        n_symbols = int(sys.argv[1])
        outpath = sys.argv[2]
        
        generate_permutation_graph(n_symbols, outpath)

    else:
        raise RuntimeError("Must provide the number of symbols as an argument")

if __name__ == "__main__":
    main()
