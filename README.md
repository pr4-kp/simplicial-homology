# Simplicial Homology Algorithms
An implementation of algorithms used in computational topology. Created for the MATH 551 honors project.

## Usage
### Creating a Simplicial Complex Object
`simplicialcomplex.py` implements the `SimplicialComplex` object. It can be constructed with the dimension of the complex
```python
K = SimplicialComplex(2)
```

$k$-simplices can be added by the method `add_simplex`
```python
K.add_simplex([0, 1, 2])
K.add_simplex([1, 2])
K.add_simplex([1])
```

### Topological Invariants
The Euler characteristic of a `SimplicialComplex` $K$ by calling 
```python
K.euler_characteristic()
```

A list of Betti numbers up to the dimension of $K$ is returned by calling
```python
K.betti_numbers()
```

## Tests
In the `test.py` file, there are example calculations done on the $2$-sphere $\mathbb{S}^2$ and the torus $\mathbb{T}^2$.

## Todo:
- [x] Simplex data structure
  - [ ] Make a filetype for data structure
- [x] Implement boundary operator (matrix)
- [x] Betti number algorithms
- [ ] Compute invariants for other simplicial complexes
