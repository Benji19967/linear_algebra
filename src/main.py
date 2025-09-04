import time
from enum import Enum

import jax.numpy as jnp
import numpy as np
import scipy.linalg
import torch

N = 10000

# np.__config__.show()


class Lib(str, Enum):
    NP = "np"
    JNP = "jnp"
    TORCH = "torch"


def solve(A, b, lib: Lib):
    if lib == Lib.TORCH:
        device = "mps"
        A = torch.randn(10000, 10000, device=device)
        b = torch.randn(10000, device=device)

    s = time.time()
    match lib:
        case Lib.JNP:
            x = jnp.linalg.solve(A, b).block_until_ready()
        case Lib.TORCH:
            x = torch.linalg.solve(A, b)
        case Lib.NP:
            x = np.linalg.solve(A, b)
    print(f"Took {time.time() - s} seconds for {lib}")

    return x


def test_performance():
    A = np.random.randint(0, 10, size=(N, N))
    b = np.random.randint(0, 10, size=(N,))

    solve(A, b, Lib.NP)
    solve(A, b, Lib.JNP)
    solve(A, b, Lib.TORCH)


def main():
    A = np.array(
        [
            [43, 1, 7],
            [12, 5, 6],
            [8, 98, 10],
        ]
    )
    b = np.array([1, 2, 3])
    det_A = np.linalg.det(A)

    A_inv = np.linalg.inv(A)
    print(det_A)
    print(A_inv)
    assert np.allclose(A_inv @ A, np.eye(3))

    x1 = A_inv @ b
    print(x1)
    print(A @ x1)

    s = time.time()
    x2, residuals, rank, singular_values = np.linalg.lstsq(A, b)
    print(f"Took {time.time() - s} seconds for least squares")
    print(x2)

    Q = scipy.linalg.orth([[1, 2], [9, 3]])
    print(Q.T @ Q)

    lu = scipy.linalg.lu([[1, 2], [9, 3]])
    print(lu)

    symmetric_matrix = np.array(
        [
            [1, 2, 3],
            [2, 5, 6],
            [3, 6, 9],
        ]
    )
    eigenvalues, Q = np.linalg.eig(symmetric_matrix)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", Q)

    assert np.allclose(Q.T @ Q, np.eye(3))


if __name__ == "__main__":
    # test_performance()
    main()
