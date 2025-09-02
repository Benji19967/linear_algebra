import numpy as np

from src.utils.timer import Timer

# Note: F_50 = 12,586,269,025


def F_k(k: int = 50) -> int:
    """
    Linear algebra:

    A = S@LAMBDA@S_inv

    u_k = A^k@u_0
    u_0 = [
        1, # F_1
        0, # F_0
    ]
    u_k = [
        F_k+1,
        F_k,
    ]

    System:
    F_k+1 = F_k + F_k-1
    F_k = F_k
    """
    A = np.array(
        [
            [1, 1],
            [1, 0],
        ],
    )
    # Option 1
    F_k_option_1 = None
    with Timer():
        F_kp1, F_k = np.linalg.matrix_power(A, k) @ np.array([[1], [0]])
        F_k_option_1 = F_k[0]

    # Option 2
    F_k_option_2 = None
    with Timer():
        (lambda_1, lambda_2), S = np.linalg.eig(A)

        LAMBDA_k = np.array([[lambda_1**k, 0], [0, lambda_2**k]])
        S_inv = np.linalg.inv(S)
        A_k = S @ LAMBDA_k @ S_inv
        F_kp1, F_k = A_k @ np.array([[1], [0]])
        F_k_option_2 = F_k[0]

    assert F_k_option_1 == int(F_k_option_2)
    return F_k_option_1


if __name__ == "__main__":
    k = 50
    print(F_k(k))
