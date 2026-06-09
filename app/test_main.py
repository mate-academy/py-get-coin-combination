import app.main as main


def test_return_0_coins_when_0_cents() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_return_1_penny_when_1_cents() -> None:
    assert main.get_coin_combination(1) == [1, 0, 0, 0]


def test_return_penny_and_nickel_when_6_cents() -> None:
    assert main.get_coin_combination(6) == [1, 1, 0, 0]


def test_return_penny_nickel_dime_when_17_cents() -> None:
    assert main.get_coin_combination(17) == [2, 1, 1, 0]


def test_return_dime_penny_when_24_cents() -> None:
    assert main.get_coin_combination(24) == [4, 0, 2, 0]


def test_return_quarter_and_penny_when_26_cents() -> None:
    assert main.get_coin_combination(26) == [1, 0, 0, 1]


def test_return_all_type_of_coins_when_41_cents() -> None:
    assert main.get_coin_combination(41) == [1, 1, 1, 1]


def test_return_2_quarter_when_50_cents() -> None:
    assert main.get_coin_combination(50) == [0, 0, 0, 2]
