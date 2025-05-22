import pytest


def urlify(s: str, num: int) -> str:
    return s.rstrip().replace(' ', '%20')


@pytest.mark.parametrize(
    "s, num, expected", [
        ("Mr John Smith   ", 13, "Mr%20John%20Smith"),
    ],
)
def test(s: str, num: int, expected: str):
    assert urlify(s, num) == expected
