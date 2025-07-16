from app.main import get_coin_combination


def test_should_return_only_pennies_for_small_amount() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_should_return_only_nickels_when_divisible_by_5() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_only_dimes_when_divisible_by_10() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_should_return_only_quarters_when_divisible_by_25() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_all_zeros_when_cents_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_valid_combination_for_large_amount() -> None:
    assert get_coin_combination(1234) == [4, 1, 0, 49]


def test_should_return_correct_total_sum() -> None:
    coins = get_coin_combination(123)
    total = (coins[0] * 1 + coins[1] * 5 + coins[2] * 10 + coins[3] * 25)

    assert total == 123
