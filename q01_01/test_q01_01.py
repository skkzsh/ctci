#!/usr/bin/env python

import pytest
import collections


def is_unique(s: str) -> bool:
    return all(c <= 1 for c in collections.Counter(s).values())


@pytest.mark.parametrize(
    "s, expected", [
        ("abc123!#$%&-=^~+*;:@`,./_()[]{}<>", True),
        ("B!C!D", False),
    ]
)
def test(s: str, expected: bool):
    assert is_unique(s) == expected
