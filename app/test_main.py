from app.main import get_coin_combination


def test_should__return_zeros_when_0_cents() -> None:
    goals = get_coin_combination(0)
    assert goals == [0, 0, 0, 0]


def test_should_return_1_penny_when_1_cent() -> None:
    goals = get_coin_combination(1)
    assert goals == [1, 0, 0, 0]


def test_should_return_1_nickle_when_5_cents() -> None:
    goals = get_coin_combination(5)
    assert goals == [0, 1, 0, 0]


def test_should_return_1_dime_when_10_cents() -> None:
    goals = get_coin_combination(10)
    assert goals == [0, 0, 1, 0]


def test_should_return_1_quarter_when_25_cents() -> None:
    goals = get_coin_combination(25)
    assert goals == [0, 0, 0, 1]


def test_should_return_different_coins() -> None:
    goals = get_coin_combination(41)
    assert goals == [1, 1, 1, 1]
