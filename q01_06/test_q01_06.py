import pytest


def compress_string(original: str) -> str:
    compressed = ''
    count = 0

    for i in range(len(original)):
        if i == len(original) - 1 or original[i] != original[i + 1]:
            compressed += original[i] + str(count + 1)
            count = 0
        else:
            count += 1

    return min(compressed, original, key=len)


@pytest.mark.parametrize(
    "original, expected", [
        ("aabcccccaaa", "a2b1c5a3"),
        ("aabcca", "aabcca"),
    ],
)
def test(original: str, expected: bool):
    assert compress_string(original) == expected
