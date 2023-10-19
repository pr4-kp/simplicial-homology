import numpy as np

EPS = 1e-9
class SimplicialComplex: 
    simplicialComplex: list[set[list[int]]] = []

    def __init__(self, dimension: int) -> None:
        self.simplicialComplex = [{}] * dimension

    def add_simplex(self, simplex: list[int]) -> None: 
        self.simplicialComplex[len(simplex)].add(simplex)

    def get_n_simplices(self, n: int) -> set[list[int]]:
        return self.simplicialComplex[n]
    
    # TODO: Gaussian elimination matrix rank
    def __matrix_rank(M: np.NdArray) -> int:
        n = len(M) # number of rows
        m = len(M[0]) # number of columns

        rank: int = 0

        row_selected = [False] * n

        # go through columns
        for i in range(m):

            # go through rows
            for j in range(n):

                # Go to the first not selected and nonzero element in column i
                if (not row_selected[j] and abs(M[j][i]) > EPS) : 
                    break

            if j != i:
                rank += 1
                row_selected[j] = True
                for p in range(i+1, m): 
                    M[j][p] /= M[j][i]
                for k in range(0, n):
                    if k != j and abs(M[k][i]) > EPS:
                        for p in range(i+1, m):
                            M[k][p] -= M[j][p] * M[k][i]
        
        return rank

    # TODO: boundary function
    def boundary(self, k: int):
        # boundary: k-simplices -> k-1-simplies
        # return a matrix from span{k-simplices} -> span(k-1-simplices)
        # simplices 
        ...

