# LU Decomposition

- Decompose `A=LU` where `L` is lower triangular and `R` upper triangular (A is nxn)
  - O(n^3)

- Key insight:
    - Solving `Ax=b` is O(n^3)
    - Solving `LUx=b` is O(n^2)

So, if we need to solve system where A is constant but b changes (example, time dependent system where b evolves over time),
then solving `Ax=b` `r` times is O(rn^3) but solving `LUx=b` `r` times is O(n^3 + rn^2).
