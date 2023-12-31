import numpy as np

EPS = 1e-9


class SimplicialComplex:
    simplicialComplex: list[list[list[int]]] = []

    def __init__(self, dimension: int) -> None:
        self.dimension = dimension + 1
        self.simplicialComplex = [[] for _ in range(self.dimension)]

    def add_simplex(self, simplex: list[int]) -> None:
        self.simplicialComplex[len(simplex) - 1].append(sorted(simplex))

    def get_k_simplices(self, k: int) -> list[list[int]]:
        return self.simplicialComplex[k]

    # source: https://code.activestate.com/recipes/578227-generate-the-parity-or-sign-of-a-permutation/
    def perm_parity(self, permutation: list[int]) -> int:
        """
        Given a permutation of the digits 0..N in order as a list,
        returns its parity (or sign): +1 for even parity; -1 for odd
        and sorts the list.
        """
        parity = 1
        for i in range(0, len(permutation) - 1):
            if permutation[i] != i:
                parity *= -1
                mn = min(range(i, len(permutation)),
                         key=permutation.__getitem__)
                permutation[i], permutation[mn] = permutation[mn], permutation[i]
        return parity

    def boundary(self, k: int) -> np.ndarray:
        """
        boundary: k-simplices -> k-1-simplies
        return a matrix from span{k-simplices} -> im(boundary)
        note that the k-simplices have k+1 entries
        """
        basis_map = (
            dict()
        )  # pair each basis element with an integer i so we can make a vector
        basis_n = 0

        k_simplices: set[tuple[int]] = self.get_k_simplices(k)

        for simplex in k_simplices:
            # each simplex will have length k

            for h in range(k + 1):
                # consider the list without the hth element
                boundary_simplex = tuple(
                    sorted(simplex[:h] + simplex[(h + 1):]))

                # boundary_simplex should now be sorted; we make this the canonical form
                # and add it to the basis
                if boundary_simplex not in basis_map:
                    basis_map[boundary_simplex] = basis_n
                    basis_n += 1

        # print(basis_map)
        M = np.zeros([len(k_simplices), len(basis_map)])

        for i, simplex in enumerate(k_simplices):
            row_vector: list[int] = [0] * len(basis_map)

            for h in range(k + 1):
                # consider the list without the hth element
                boundary_simplex = simplex[:h] + simplex[(h + 1):]
                # print(boundary_simplex)

                sgn = self.perm_parity(boundary_simplex)
                boundary_simplex.sort()

                row_vector[basis_map[tuple(
                    boundary_simplex)]] = sgn * (-1) ** h

            # With each row vector, we add it to a matrix M
            M[i] = row_vector
        return M

    def boundary_rank(self, k: int) -> int:
        return np.linalg.matrix_rank(self.boundary(k))

    def betti_numbers(self) -> int:
        b = [len(self.get_k_simplices(0)) - self.boundary_rank(1)]

        for j in range(1, self.dimension-1):

            b.append(len(self.get_k_simplices(j)) -
                     self.boundary_rank(j) - self.boundary_rank(j+1))

        b.append(len(self.get_k_simplices(self.dimension-1)) -
                 self.boundary_rank(self.dimension-1))
        return b

    def euler_characteristic(self) -> int:
        return sum([x * (-1)**i for i, x in enumerate(self.betti_numbers())])
