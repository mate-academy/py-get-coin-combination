import pytest

from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_only_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_only_pennies_and_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_quarters_and_remainder() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_multiple_quarters() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_mixed_change() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_large_value() -> None:
    assert get_coin_combination(1000) == [0, 0, 0, 40]


@pytest.mark.parametrize("invalid_input", ["10", {}, None, [9]])
def test_invalid_types_raise_typeerror(invalid_input: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(invalid_input)


def test_negative_value() -> None:
    assert get_coin_combination(-5) == [0, 0, 2, -1]
