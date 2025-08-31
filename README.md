# Linear Algebra

## Performance (Mac M1)

- A is NxN
- N = 10_000

Then, `Ax=b` is solved in 

- 2.65 seconds for jnp (jax)
- 3.90 seconds for torch (using `mps`)
- 8.04 seconds for numpy

## Method

- `np.linalg.solve`  O(n^3): uses LU decomposition
    - A must be _square_ and _well-conditioned_, so _not singular_
- `np.linalg.lstsq`  O(n^3): uses QR decomposition (slower)
    - A can be rectangular