#!/usr/bin/env python

import pytest


def is_one_away(sfrom: str, sto: str) -> bool:
    return False


@pytest.mark.parametrize(
    "sfrom, sto, expected", [
        ("pale", "ple", True),
        ("pale", "pales", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
    ]
)
def test(sfrom: str, sto: str, expected: bool):
    assert is_one_away(sfrom, sto) == expected
