import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination_with_valid_input(
    cents: int, expected: list
) -> None:
    assert get_coin_combination(cents) == expected


def test_should_return_zeros_when_cents_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
    ],
)
def test_should_use_correct_denomination_at_boundaries(
    cents: int, expected: list
) -> None:
    assert get_coin_combination(cents) == expected


def test_sum_of_coins_should_equal_cents() -> None:
    cents = 87
    result = get_coin_combination(cents)
    total = (
        result[0] * 1
        + result[1] * 5
        + result[2] * 10
        + result[3] * 25
    )
    assert total == cents


def test_get_coin_combination_should_return_list() -> None:
    result = get_coin_combination(17)
    assert isinstance(result, list)


def test_get_coin_combination_should_return_four_elements() -> None:
    result = get_coin_combination(17)
    assert len(result) == 4
