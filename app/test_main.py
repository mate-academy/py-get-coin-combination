from app.main import get_coin_combination


def test_should_return_zeros_when_cents_is_0() -> None:
    result = get_coin_combination(0)
    assert result == [0, 0, 0, 0]


def test_should_return_one_pennie_when_cents_is_1() -> None:
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0]


def test_should_return_one_nickel_when_cents_is_5() -> None:
    result = get_coin_combination(5)
    assert result == [0, 1, 0, 0]


def test_should_return_one_dime_when_cents_is_10() -> None:
    result = get_coin_combination(10)
    assert result == [0, 0, 1, 0]


def test_should_return_one_quarter_when_cents_is_25() -> None:
    result = get_coin_combination(25)
    assert result == [0, 0, 0, 1]


def test_get_coin_combination_returns_mixed_coins() -> None:
    result = get_coin_combination(41)
    assert result == [1, 1, 1, 1]
