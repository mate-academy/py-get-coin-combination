import pytest
from app.main import get_coin_combination


def test_with_negative_value() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-10)


def test_with_only_penny() -> None:
    assert get_coin_combination(2) == [2, 0, 0, 0]


def test_with_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_with_penny_nickel_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_with_every_possible_value() -> None:
    assert get_coin_combination(67) == [2, 1, 1, 2]
