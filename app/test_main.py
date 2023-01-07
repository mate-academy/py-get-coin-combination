from app.main import get_coin_combination


def test_should_return_zeros_when_0_cents() -> None:
    cents = 0

    result_list = get_coin_combination(cents)

    assert result_list == [0, 0, 0, 0]


def test_should_return_1_penny_when_1_cent() -> None:
    cents = 1

    result_list = get_coin_combination(cents)

    assert result_list == [1, 0, 0, 0]


def test_should_return_1_penny_1_nickel_when_6_cents() -> None:
    cents = 6

    result_list = get_coin_combination(cents)

    assert result_list == [1, 1, 0, 0]


def test_should_return_2_pennies_1_nickel_1_dime_when_17_cents() -> None:
    cents = 17

    result_list = get_coin_combination(cents)

    assert result_list == [2, 1, 1, 0]


def test_should_return_2_quarters_when_50_cents() -> None:
    cents = 50

    result_list = get_coin_combination(cents)

    assert result_list == [0, 0, 0, 2]
