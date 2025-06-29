import pytest
import collections


def sut(s: str) -> bool:
    return len([c for c in collections.Counter(s.replace(" ", "").lower()).values() if c % 2 == 1]) <= 1


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Tact Ca", True),
        ("Tact Coa", True),
        ("Fact Coa", False),
    ],
)
def test(s: str, expected: bool):
    assert sut(s) == expected
