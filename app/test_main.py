from app.main import get_coin_combination


def test_1_penny() -> None:
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0]


def test_1_penny_1_nickel() -> None:
    result = get_coin_combination(6)
    assert result == [1, 1, 0, 0]


def test_2_pennies_1_nickel_1_dime() -> None:
    result = get_coin_combination(17)
    assert result == [2, 1, 1, 0]


def test_2_quarters() -> None:
    result = get_coin_combination(50)
    assert result == [0, 0, 0, 2]
