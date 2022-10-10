#!/usr/bin/env python

import copy
from typing import List
import pytest


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    m = len(matrix[0])
    n = len(matrix)
    result = copy.deepcopy(matrix)
    zero_rows = set()
    zero_cols = set()

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
    )]
)
def test(matrix: List[List[int]], expected: List[List[int]]):
    assert zero_matrix(matrix) == expected
