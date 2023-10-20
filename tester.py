import SimplicialComplex

if __name__ == "__main__":
    simplex = SimplicialComplex.SimplicialComplex(4)

    for j in range(4):
        simplex.add_simplex([j])

    simplex.add_simplex([0, 1])
    simplex.add_simplex([0, 2])
    simplex.add_simplex([0, 3])
    simplex.add_simplex([1, 2])
    simplex.add_simplex([1, 3])
    simplex.add_simplex([2, 3])

    simplex.add_simplex([1, 2, 3])
    simplex.add_simplex([2, 3, 4])
    simplex.add_simplex([1, 3, 4])

    simplex.add_simplex([1, 2, 3, 4])

    # print(f"the 0-simplices are {simplex.get_k_simplices(0)}")
    # print(f"the 1-simplices are {simplex.get_k_simplices(1)}")

    i = 1
    print(f"The rank of the {i}-boundary map is {simplex.boundary_rank(i)}")
    i = 2
    print(f"The rank of the {i}-boundary map is {simplex.boundary_rank(i)}")
    print(f"The betti numbers are {simplex.betti_numbers()}")
