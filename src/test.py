import unittest
from metrics import permutation_distance

perm_distance_pairs = [
    (('123', '123'), 0),
    (('123', '312'), 2),
    (('1234', '4312'), 3),
    (('162534', '534612'), 3),
]


class TestDistanceMetric(unittest.TestCase):

    def test_distance(self):
        for (p1, p2), true_dist in perm_distance_pairs:
            dist = permutation_distance(p1, p2)
            self.assertEqual(dist, true_dist)


if __name__ == '__main__':
    unittest.main()