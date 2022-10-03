#!/usr/bin/env python

import collections
import pytest

def sut(s: str) -> bool:
    return all(c <= 1 for c in collections.Counter(s).values())

@pytest.mark.parametrize(
    "s, expected", [
        ("abcde", True),
        ("aaaaa", False),
        ("bacad", False),
    ]
)
def test(s: str, expected: bool):
    assert sut(s) == expected

