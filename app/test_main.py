from app.main import get_coin_combination


def test_value_should_be_equal_to_1() -> None:
    result = get_coin_combination(cents=1)
    assert (
        result == [1, 0, 0, 0],
    ), f"For cents=1, expected [1, 0, 0, 0], but got {result}"


def test_value_should_be_equal_to_5() -> None:
    result = get_coin_combination(cents=5)
    assert (
        result == [0, 1, 0, 0],
    ), f"For cents=5, expected [0, 1, 0, 0], but got {result}"


def test_value_should_be_equal_to_10() -> None:
    result = get_coin_combination(cents=10)
    assert (
        result == [0, 0, 1, 0],
    ), f"For cents=10, expected [0, 0, 1, 0], but got {result}"


def test_value_should_be_equal_to_25() -> None:
    result = get_coin_combination(cents=25)
    assert (
        result == [0, 0, 0, 1],
    ), f"For cents=25, expected [0, 0, 0, 1], but got {result}"


def test_should_return_different_coins() -> None:
    result = get_coin_combination(cents=6)
    assert (
        result == [1, 1, 0, 0],
    ), f"For cents=6, expected [1, 1, 0, 0], but got {result}"


def test_return_coins_of_the_different_types() -> None:
    result = get_coin_combination(cents=17)
    assert (
        result == [2, 1, 1, 0],
    ), f"For cents=17, expected [2, 1, 0, 0], but got {result}"
