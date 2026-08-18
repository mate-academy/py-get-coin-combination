from app.main import get_coin_combination


def test_should_return_zero_when_zero_cent() -> None:
    assert get_coin_combination(0) == [0, 0 , 0, 0]


def test_should_return_one_when_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0 , 0]


def test_should_return_four_when_four_cents() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_return_1_nickel_when_5_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_1_nickel_and_four_cents_when_9_cents() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_should_return_1_dime_when_10_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_2_dime_when_24_cents() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_should_return_1_quarter_when_25_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
