import SimplicialComplex
import unittest


class TwoSphere:
    simplex = SimplicialComplex.SimplicialComplex(2)

    for j in range(4):
        simplex.add_simplex([j])

    simplex.add_simplex([0, 1])
    simplex.add_simplex([0, 2])
    simplex.add_simplex([0, 3])
    simplex.add_simplex([1, 2])
    simplex.add_simplex([1, 3])
    simplex.add_simplex([2, 3])

    simplex.add_simplex([2, 3, 1])
    simplex.add_simplex([2, 3, 4])
    simplex.add_simplex([1, 3, 4])
    simplex.add_simplex([1, 2, 4])


class Torus:
    simplex = SimplicialComplex.SimplicialComplex(2)

    for j in range(1, 8):
        simplex.add_simplex([j])

    simplex.add_simplex([1, 4])
    simplex.add_simplex([1, 3])

    simplex.add_simplex([4, 6])
    simplex.add_simplex([4, 5])
    simplex.add_simplex([4, 7])
    simplex.add_simplex([3, 4])

    simplex.add_simplex([5, 7])
    simplex.add_simplex([5, 1])
    simplex.add_simplex([1, 7])

    simplex.add_simplex([3, 2])
    simplex.add_simplex([3, 6])
    simplex.add_simplex([3, 5])
    simplex.add_simplex([3, 7])

    simplex.add_simplex([6, 7])
    simplex.add_simplex([6, 2])
    simplex.add_simplex([6, 5])
    simplex.add_simplex([6, 1])

    simplex.add_simplex([7, 2])

    simplex.add_simplex([2, 1])
    simplex.add_simplex([2, 4])
    simplex.add_simplex([2, 5])

    simplex.add_simplex([1, 4, 3])
    simplex.add_simplex([3, 4, 6])
    simplex.add_simplex([4, 6, 7])
    simplex.add_simplex([4, 5, 7])
    simplex.add_simplex([1, 5, 7])
    simplex.add_simplex([1, 3, 7])
    simplex.add_simplex([3, 5, 6])
    simplex.add_simplex([3, 2, 5])
    simplex.add_simplex([2, 4, 5])
    simplex.add_simplex([5, 6, 1])
    simplex.add_simplex([2, 1, 4])
    simplex.add_simplex([2, 7, 6])
    simplex.add_simplex([2, 3, 7])
    simplex.add_simplex([1, 2, 6])


class TestSimplex(unittest.TestCase):
    def test_betti_numbers(self):
        self.assertEqual(TwoSphere.simplex.betti_numbers(), [1, 0, 1])
        self.assertEqual(Torus.simplex.betti_numbers(), [1, 2, 1])

    def test_euler_characteristic(self):
        self.assertEqual(TwoSphere.simplex.euler_characteristic(), 2)
        self.assertEqual(Torus.simplex.euler_characteristic(), 0)


if __name__ == "__main__":
    unittest.main()
