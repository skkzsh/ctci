#!/usr/bin/env python

import pytest


def is_one_away(sfrom: str, sto: str) -> bool:
    if len(sfrom) - len(sto) == 1:
        return is_one_away_plus(sfrom, sto)
    elif len(sfrom) - len(sto) == -1:
        return is_one_away_plus(sto, sfrom)
    elif len(sfrom) - len(sto) == 0:
        return sfrom == sto
    return False

def is_one_away_plus(longer: str, shorter: str) -> bool:
    if len(longer) - len(shorter) != 1:
        return False

    c = (set(longer) - set(shorter)).pop()
    for i in range(len(shorter) + 1):
        candidate = shorter[:i] + c + shorter[i:]
        if candidate == longer:
            return True

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
