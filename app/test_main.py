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
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_get_coin_combination_valid_cases(
        cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_all_types() -> None:
    result = get_coin_combination(41)
    assert result == [1, 1, 1, 1]
    assert all(x > 0 for x in result)


def test_get_coin_combination_three_types() -> None:
    result = get_coin_combination(17)
    assert result[0] > 0 and result[1] > 0 and result[2] > 0


def test_get_coin_combination_two_types() -> None:
    result = get_coin_combination(30)
    assert result[1] > 0 and result[3] > 0


@pytest.mark.parametrize(
    "cents",
    [
        -1,
        "ten",
        10.5,
    ],
)
def test_get_coin_combination_invalid_inputs(cents: object) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_coin_combination(cents)
