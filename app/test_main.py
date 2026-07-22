from app.main import get_coin_combination


def test_should_return_0_when_cents_is_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_result_equal_cents() -> None:
    result = get_coin_combination(2378)
    assert (result[0] + result[1] * 5
            + result[2] * 10 + result[3] * 25 == 2378)


def test_should_return_smallest_possible_coins_when_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_smallest_possible_coins_when_20_cents() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_should_return_smallest_possible_coins_when_10_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_smallest_possible_coins_when_5_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
