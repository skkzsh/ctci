#!/usr/bin/env python

import pytest


def is_permutaion(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


@pytest.mark.parametrize(
    "s1, s2, expected", [
        ("[abc123]", "][1c2b3a", True),
        ("D!C!B", "BCD!", False),
        ("!BCD", "D!C!B", False),
    ]
)
def test(s1: str, s2: str, expected: bool):
    assert is_permutaion(s1, s2) == expected
