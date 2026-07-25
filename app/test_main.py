from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_smallest_unit_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_nickel_combination() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_dime_combination() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(11) == [1, 0, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_quarter_combination() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(26) == [1, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_complex_combination_large_value() -> None:
    assert get_coin_combination(97) == [2, 0, 2, 3]


def test_sum_of_combination_equals_cents() -> None:
    test_cases = [1, 6, 17, 50, 99, 32, 100]
    values = [1, 5, 10, 25]

    for cents_value in test_cases:
        coins = get_coin_combination(cents_value)
        total = sum(coins[i] * values[i] for i in range(4))
        assert total == cents_value


def test_just_under_next_coin() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]
    assert get_coin_combination(24) == [4, 0, 2, 0]
    assert get_coin_combination(49) == [4, 0, 2, 1]
