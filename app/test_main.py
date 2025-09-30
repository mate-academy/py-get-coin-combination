import pytest
from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_nine_cents() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_twenty_four_cents() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_twenty_five_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_large_value() -> None:
    result = get_coin_combination(99)
    expected = [4, 0, 2, 3]
    assert result == expected


@pytest.mark.parametrize("cents", [0, 1, 6, 17, 50, 99, 1234])
def test_total_value(cents: int) -> None:
    result = get_coin_combination(cents)
    values = [1, 5, 10, 25]
    total = sum(c * v for c, v in zip(result, values))
    assert total == cents, f"Expected total {cents}, got {total}"


def test_minimum_number_of_coins() -> None:
    result = get_coin_combination(41)
    assert result == [1, 1, 1, 1]
