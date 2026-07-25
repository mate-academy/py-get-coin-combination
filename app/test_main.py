from app.main import get_coin_combination


# write your tests here
def test_should_1_penny_when_cents_equal_1() -> None:
    result = get_coin_combination(1)

    assert result == [1, 0, 0, 0]


def test_should_1_nickel_when_cents_equal_5() -> None:
    result = get_coin_combination(6)

    assert result == [1, 1, 0, 0]


def test_should_1_dime_when_cents_equal_10() -> None:
    result = get_coin_combination(17)

    assert result == [2, 1, 1, 0]


def test_should_1_quarter_when_cents_equal_25() -> None:
    result = get_coin_combination(50)

    assert result == [0, 0, 0, 2]
