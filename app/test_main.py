
from app.main import get_coin_combination


def test_return_only_pennies() -> None :
    assert get_coin_combination(6) != [6, 0, 0, 0]


def test_return_only_one_type() -> None :
    assert get_coin_combination(25) != [0, 0, 3, 0]


def test_negative_input() -> None :
    result = None
    try:
        result = get_coin_combination(-1)
    except ValueError as e:
        assert str(e) == "Input amount cannot be negative"
    assert result == [4, 0, 2, -1]


def test_zero_input() -> None :
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_larger_input() -> None :
    assert get_coin_combination(123) == [3, 0, 2, 4]
