"""
Generate the distance matrix for permutations of n symbols.

The script creates the n,n-matrix in which the entry at position 
i,j is the permutation distance between permutations i and j. 
The indices maps to the permutations stored in an array 
that is created alongside the matrix.

The matrix and list are stored to a file given by the user.

Usage:
    python generate_matrix.py <number of symbols> <ouput path>

where
    <number of symbols> : number of symbols to permute.
    <ouput path> : file to which the output should be saved.
"""
import sys
from itertools import permutations, combinations
import numpy as np
from metrics import overlap_distance


def generate_distance_matrix(n_symbols, file_path):
    symbols = map(str, range(1, n_symbols + 1))
    perms = [''.join(p) for p in permutations(symbols)]

    n_perms = len(perms)

    distance_matrix = np.empty((n_perms, n_perms), 
                               dtype=np.int8)

    for i in range(n_perms):
        for j in range(n_perms):
            if i != j:
                dist = overlap_distance(perms[i], perms[j])
            else:
                dist = 0

            distance_matrix[i, j] = dist

    np.savez(file_path, 
             permutations=perms, 
             distance_matrix=distance_matrix)


def main():
    if len(sys.argv) == 3:
        n_symbols = int(sys.argv[1])
        outpath = sys.argv[2]
        
        generate_distance_matrix(n_symbols, outpath)

    else:
        raise RuntimeError("Must provide the number of symbols as an argument")

if __name__ == "__main__":
    main()
