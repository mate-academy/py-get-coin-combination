from app.main import get_coin_combination


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_mixed_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_dime_for_ten() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_complex_amount() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_one_each() -> None:
    # 25 + 10 + 5 + 1 = 41
    assert get_coin_combination(41) == [1, 1, 1, 1]

