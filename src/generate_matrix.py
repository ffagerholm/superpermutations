import sys
from itertools import permutations, combinations
import numpy as np


def distance(seq1, seq2):
    assert len(seq1) == len(seq2)
    n = len(seq1)

    for i in range(len(seq1)):
        if seq1[i:] == seq2[:n - i]:
            return i
    return n


def generate_distance_matrix(n_symbols, file_path):
    symbols = map(str, range(1, n_symbols + 1))
    perms = [''.join(p) for p in permutations(symbols)]

    n_perms = len(perms)

    distance_matrix = np.empty((n_perms, n_perms), 
                               dtype=np.float16)

    for i in range(n_perms):
        for j in range(n_perms):
            if i != j:
                dist = distance(perms[i], perms[j])
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
