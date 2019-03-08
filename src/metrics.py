
def overlap_distance(p1, p2):
    """Measures the distance between two sequences of symbols.

    The distance beetween two sequences is measued as the number of 
    symbols that has to be concatenated to the second, and equally
    many removed from the start of the sequence, to transform it
    to the second sequence.

    For example, for the distance between the sequences 123 and 312 
    is 2, because 123 -> [12]3 . 12 -> 312  
    The brackets indicates that the substring "12" is removed, and the
    dot that the string "12" is concatenated.

    For 132, and 231 it is 2:
    132 -> [13]2 . 31 -> 231

    For 162534 and 534612 it is 3:
    162534 -> [162]534 . 612 -> 534612

    Note that this is not a true distance metric since it is 
    not symmetric, for some p1, p2: distance(p1, p2) != distance(p2, p1).

    Args:
        p1 (str): first sequence, could be a string, list
        p2 (str): second sequence
    
    Returns:
        distance (int): overlap distance.

    >>> overlap_distance("1234", "1234")
    0
    >>> overlap_distance("1234", "4321")
    1
    >>> overlap_distance("123", "312")
    2
    >>> overlap_distance("132", "231")
    2
    >>> overlap_distance("162534", "534612")
    3
    """
    n, m = len(p1), len(p2)
    assert n == m

    for i in range(n):
        if p1[i:] == p2[:n - i]:
            return i
    return n
