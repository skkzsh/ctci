from typing import Final

import pytest


def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    n: Final = len(matrix)
    return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]


@pytest.mark.parametrize(
    "matrix, expected", [(
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5]
            ]
    )],
)
def test(matrix: list[list[int]], expected: list[list[int]]):
    assert rotate_matrix(matrix) == expected
