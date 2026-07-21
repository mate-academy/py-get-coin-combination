import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert isinstance(cents, int), \
        "the cents must be an integer"
    assert cents >= 0, \
        "the cents must be positive"
    assert isinstance(get_coin_combination(cents), list), \
        "the result must be a type list"
    assert len(get_coin_combination(cents)) == 4, \
        "the result must have 4 elements"
    assert all(isinstance(num, int) for num in get_coin_combination(cents)), \
        "all elements must be integers"
    assert get_coin_combination(cents) == expected, \
        "the result must be the expected one"
