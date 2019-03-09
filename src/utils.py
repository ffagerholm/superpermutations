
from itertools import permutations

def list_permutations(n):
    """Generates a list of all permutations.
    Returns a list of all permutations of n symbols, as strings.
    Args:
        n (int): number of symbols to permute.
    
    Returns:
        list(str): list of permutations.

    >>> list_permutations(2)
    ['12', '21']
    """
    symbols = map(str, range(1, n + 1))
    perms = [''.join(p) for p in permutations(symbols)]
    return perms


def is_superstring(strings, superstring):
    """Checks if all strings in a list are contained in another string.
    For example 'abcde' is a superstring of 'abc', 'bc' and 'de', so
    is_superstring(['abc', 'bc', 'de'], 'abcde) == True

    Args:
        strings (list(str)): List of strings.
        superstring (str): String to check against.
    Returns:
        is_superstring (bool)

    >>> is_superstring(['a', 'bc', 'abc'], 'abc')
    True
    >>> is_superstring(['a', 'd'], 'abc')
    False
    """
    return all(s in superstring for s in strings)


def expand_superpermutation(superpermutation):
    """Generates a list of permutations from a superpermutation.
    The permutations will be listed in the same order as they appear in
    the superpermutation.

    Args:
        superpermutation (str): Sequence of symbols containing 
            all permutations of those symbols as substrings.
    
    Returns:
        list(str): List of permutations.
    """
    n = len(set(superpermutation))
    if n == 1:
        return [superpermutation]

    perms = []
    for i in range(len(superpermutation) - n + 1):
        p = superpermutation[i:i+n]
        if len(set(p)) == n and not p in perms:
            perms.append(p)
    
    return perms