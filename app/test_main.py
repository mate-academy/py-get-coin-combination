from app.main import get_coin_combination


def test_should_return_zero_coins_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_only_pennies() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_should_use_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_use_nickel_and_penny() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_use_dime_correctly() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_use_dime_nickel_and_pennies() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_use_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_use_multiple_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_mix_all_coin_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_minimize_number_of_coins() -> None:
    assert get_coin_combination(30) == [0, 1, 0, 1]
