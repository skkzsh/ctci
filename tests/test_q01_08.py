from typing import Final

import pytest
import copy


def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    m: Final = len(matrix[0])
    n: Final = len(matrix)
    result: Final = copy.deepcopy(matrix)
    zero_rows: Final[set[int]] = set()
    zero_cols: Final[set[int]] = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                zero_rows.add(x)
                zero_cols.add(y)

    for x in zero_rows:
        for y in range(n):
            result[x][y] = 0

    for y in zero_cols:
        for x in range(m):
            result[x][y] = 0

    return result


@pytest.mark.parametrize(
    "matrix, expected", [(
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25]
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0]
            ]
    )],
)
def test(matrix: list[list[int]], expected: list[list[int]]):
    assert zero_matrix(matrix) == expected
