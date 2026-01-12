from app.main import get_coin_combination


def test_result_should_return_list() -> None:
    result = get_coin_combination(10)
    assert isinstance(result, list), "Result should be a list"
    assert len(result) == 4, "Result should contain exactly 4 elements"


def test_zero_cents() -> None:
    result = get_coin_combination(0)
    assert result == [0, 0, 0, 0]


def test_only_pennies() -> None:
    result = get_coin_combination(3)
    assert result == [3, 0, 0, 0]


def test_only_nickel() -> None:
    result = get_coin_combination(5)
    assert result == [0, 1, 0, 0]


def test_only_dime() -> None:
    result = get_coin_combination(10)
    assert result == [0, 0, 1, 0]


def test_only_quarter() -> None:
    result = get_coin_combination(25)
    assert result == [0, 0, 0, 1]


def test_mixed_coins_example_1() -> None:
    result = get_coin_combination(6)
    assert result == [1, 1, 0, 0]


def test_mixed_coins_example_2() -> None:
    result = get_coin_combination(17)
    assert result == [2, 1, 1, 0]


def test_total_value_is_correct() -> None:
    coins = get_coin_combination(100)
    total = coins[0] * 1 + coins[1] * 5 + coins[2] * 10 + coins[3] * 25
    assert total == 100


def test_minimal_number_of_coins() -> None:
    result = get_coin_combination(50)
    assert result != [50, 0, 0, 0]
