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

    c = str_diff(longer, shorter)
    for i in range(len(shorter) + 1):
        candidate = shorter[:i] + c + shorter[i:]
        if candidate == longer:
            return True

    return False


def is_one_away_equal(s1: str, s2: str) -> bool:
    if len(s1) - len(s2) != 0:
        return False

    only1 = str_diff(s1, s2)
    only2 = str_diff(s2, s1)

    if len(only1) != 1 or len(only2) != 1:
        return False

    for i in range(len(s2) + 1):
        candidate = s2[:i] + only1 + s2[i + 1:]
        if candidate == s1:
            return True

    return False


def str_diff(s1: str, s2: str) -> str:
    result = str(s1)
    for s in s2:
        result = result.replace(s, "", 1)
    return result


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
def test_is_one_away(sfrom: str, sto: str, expected: bool):
    assert is_one_away(sfrom, sto) == expected


@pytest.mark.parametrize(
    "s1, s2, expected", [
        ("pale", "ale", "p"),
        ("pale", "apale", ""),
        ("pale", "bale", "p"),
        ("pale", "pal", "e"),
        ("pale", "palee", ""),
        ("pale", "pala", "e"),
        ("pale", "bake", "pl"),
    ]
)
def test_str_diff(s1: str, s2: str, expected: str):
    assert str_diff(s1, s2) == expected
