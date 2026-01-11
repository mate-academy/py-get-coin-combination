from app.main import get_coin_combination


def test_amount_in_cents_1() -> None:
    goals = get_coin_combination(1)
    assert goals == [1, 0, 0, 0]


def test_amount_in_cents_6() -> None:
    goals = get_coin_combination(6)
    assert goals == [1, 1, 0, 0]


def test_amount_in_cents_17() -> None:
    goals = get_coin_combination(17)
    assert goals == [2, 1, 1, 0]


def test_amount_in_cents_50() -> None:
    goals = get_coin_combination(50)
    assert goals == [0, 0, 0, 2]
