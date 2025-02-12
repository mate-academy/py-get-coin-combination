from app.main import get_coin_combination


def test_no_money() -> None:
    result = get_coin_combination(0)
    assert result == [0, 0, 0, 0]


def test_should_return_1_penny() -> None:
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0]


def test_should_return_1_penny_and_nickel() -> None:
    result = get_coin_combination(6)
    assert result == [1, 1, 0, 0]


def test_should_return_2_pennies_1_nickel_and_1_dime() -> None:
    result = get_coin_combination(17)
    assert result == [2, 1, 1, 0]


def test_should_return_2_quarters() -> None:
    result = get_coin_combination(50)
    assert result == [0, 0, 0, 2]
