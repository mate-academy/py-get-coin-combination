from app.main import get_coin_combination


def test_should_return_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_nickel_and_one_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_mix_of_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_two_quarters_for_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_no_coins_for_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_one_of_each_for_41_cents() -> None:
    # 1 penny, 1 nickel, 1 dime, 1 quarter = 41
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_large_value_example() -> None:
    # 99 cents = 3*25 + 2*10 + 0*5 + 4*1 = [4, 0, 2, 3]
    assert get_coin_combination(99) == [4, 0, 2, 3]
