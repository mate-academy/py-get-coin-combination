from app.main import get_coin_combination


def test_should_return_only_pennies_for_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_penny_and_nickel_for_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_combination_of_all_for_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_two_quarters_for_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_zero_for_0_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_correct_combination_for_99_cents() -> None:
    # 3 quarters (75) + 2 dimes (20) + 0 nickels + 4 pennies = 99
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_should_return_correct_combination_for_100_cents() -> None:
    # 4 quarters (100)
    assert get_coin_combination(100) == [0, 0, 0, 4]
