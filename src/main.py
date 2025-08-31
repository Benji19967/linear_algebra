import numpy as np


def main():
    A = np.array(
        [
            [43, 1, 7],
            [12, 5, 6],
            [8, 98, 10],
        ]
    )
    det_A = np.linalg.det(A)
    A_inv = np.linalg.inv(A)
    print(det_A)
    print(A_inv)
    assert np.allclose(A_inv @ A, np.eye(3))


if __name__ == "__main__":
    main()
