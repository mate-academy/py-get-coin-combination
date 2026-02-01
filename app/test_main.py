from app.main import get_coin_combination


def test_return_only_pennies() -> None:
    coins = get_coin_combination(3)
    assert coins == [3, 0, 0, 0]


def test_return_only_one_type() -> None:
    coins = get_coin_combination(30)
    assert coins == [0, 1, 0, 1]


def test_return_multiple_types() -> None:
    coins = get_coin_combination(17)
    assert coins == [2, 1, 1, 0]

    coins = get_coin_combination(41)
    assert coins == [1, 1, 1, 1]
