import pytest

from app import main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_should_return_expected_coin_combination(
        cents: int,
        expected: list[int]
) -> None:
    assert main.get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [
        2,
        7,
        18,
        26,
        57,
    ],
)
def test_should_return_four_integer_values(cents: int) -> None:
    result = main.get_coin_combination(cents)

    assert len(result) == 4
    assert all(type(coin) is int for coin in result)
