from app.main import get_coin_combination


def test_coin_with_0_amount() -> None:
    amount = get_coin_combination(0)
    assert amount == [0, 0, 0, 0]


def test_coin_with_1_amount() -> None:
    amount = get_coin_combination(1)
    assert amount == [1, 0, 0, 0]


def test_coin_with_50_amount() -> None:
    amount = get_coin_combination(50)
    assert amount == [0, 0, 0, 2]


def test_coin_with_17_amount() -> None:
    amount = get_coin_combination(17)
    assert amount == [2, 1, 1, 0]
