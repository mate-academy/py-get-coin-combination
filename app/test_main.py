import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_coin_combination_has_four_elements() -> None:
    result = get_coin_combination(17)

    assert len(result) == 4


def test_coin_combination_gives_exact_amount() -> None:
    cents = 87
    pennies, nickels, dimes, quarters = get_coin_combination(cents)

    total = (
        pennies * 1
        + nickels * 5
        + dimes * 10
        + quarters * 25
    )

    assert total == cents


def test_coin_combination_uses_minimum_number_of_coins() -> None:
    result = get_coin_combination(87)

    assert sum(result) == 6


def test_zero_cents_returns_empty_combination() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
