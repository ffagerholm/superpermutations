"""
Each of those permutation are then placed next to a copy of themselves 
with an nth symbol added in between the two copies

from 1 to 2
1 -> 1

1 . 2 . 1 -> 121

from 2 to 3
121 -> 12, 21

12 . 3 . 12 . 21 . 3 . 21 -> 1231221321 -> 123121321

from 3 to 4
123121321 -> 123, 231, 312, 213, 132, 321

123 . 4 . 123 . 231 . 4 . 231 . 312 . 4 . 312 . 213 . 4 . 213 . 132 . 4 . 132 . 321 . 4 . 321 ->
123412323142313124312213421313241323214321 ->
12341232314231312431213421313241323214321
"""
import sys
from itertools import groupby


def iterate_perms(superperm):
    n = len(set(superperm))
    if n == 1:
        yield superperm
        return

    seen = []
    for i in range(len(superperm) - n + 1):
        p = superperm[i:i+n]
        if len(set(p)) == n and not p in seen:
            seen.append(p)
            yield p

def remove_adjecent_duplicates(s):
    """Remove all adjecent duplicate symbols.

    >> remove_adjecent_duplicates('1221')
    '121'
    >> remove_adjecent_duplicates('2112211')
    '2121'
    """
    return ''.join(ch for ch, _ in groupby(s))


def superpermutation(n):
    """
    """
    assert n >= 1
    # base case
    if n == 1:
        return "1"
    else:
        sp = superpermutation(n - 1)
        new_sp = ""
        for p in iterate_perms(sp):
            print(p + str(n) + p)
            new_sp += p + str(n) + p 

        return remove_adjecent_duplicates(new_sp)       


if __name__ == "__main__":
    if len(sys.argv) == 2:
        n_symbols = int(sys.argv[1])
        print("Superpermutation of %d symbols:" % n_symbols, superpermutation(n_symbols))    
    else:
        raise RuntimeError("Must provide the number of symbols as an argument")

