import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (3, [3, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (40, [0, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (72, [2, 0, 2, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4])
    ])
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
