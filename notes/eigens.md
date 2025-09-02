# Eigenvalues and eigenvectors

## Properties

- eigenvalues and eigenvectors are only defined for __square__ matrices
- tr(A) = sum of eigenvalues
- det(A) = product of eigenvalues

### Projection matrix

- $\lambda_1$ = 0 (any x perpendicular to plane)
- $\lambda_2$ = 1 (any x in plane)

### Rotation matrix

- eigenvalues are complex (clearly, no non-zero vector is parallel to its original after a nontrivial rotation in $\mathbb{R}^n$)

### Triangular matrix

- eigenvalues can be read off the diagonal

## Computation
- Ax = $\lambda$ x --> finds which vectors when transformed by A, point in the same direction but scaled by $\lambda$
- Rewrite: (A - $\lambda$ I)x = 0
  - trivial solution: 
    - x = 0
  - non-trivial solution: 
    - we're looking for N(A - $\lambda$ I) (nullspace)
    - --> A - $\lambda$ I has to be singular
    - --> det(A - $\lambda$ I) = 0
    - --> compute eigenvalues
    - --> get associated eigenvectors from (A - $\lambda$ I)x = 0