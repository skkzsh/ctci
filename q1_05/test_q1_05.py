#!/usr/bin/env python

import pytest


def is_one_away(sfrom: str, sto: str) -> bool:
    if len(sfrom) - len(sto) == 1:
        return is_one_away_plus(sfrom, sto)
    elif len(sfrom) - len(sto) == -1:
        return is_one_away_plus(sto, sfrom)
    elif len(sfrom) - len(sto) == 0:
        return is_one_away_equal(sfrom, sto)
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


def is_one_away_equal(s1: str, s2: str) -> bool:
    if len(s1) - len(s2) != 0:
        return False

    only_from = set(s1) - set(s2)
    only_to = set(s2) - set(s1)

    if len(only_from) != 1 or len(only_to) != 1:
        return False

    c = only_from.pop()
    for i in range(len(s2) + 1):
        candidate = s2[:i] + c + s2[i + 1:]
        if candidate == s1:
            return True

    return False


@pytest.mark.parametrize(
    "sfrom, sto, expected", [
        ("pale", "ale", True),
        ("pale", "apale", True),
        ("pale", "bale", True),
        ("pale", "pal", True),
        ("pale", "palee", True),
        ("pale", "pala", True),
        ("pale", "bake", False),
    ]
)
def test(sfrom: str, sto: str, expected: bool):
    assert is_one_away(sfrom, sto) == expected
