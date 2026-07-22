from app.main import get_coin_combination


def test_should_return_all_0_when_coins_is_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_expected_result_when_coins_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_expected_result_when_coins_5() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_should_return_expected_result_when_coins_10() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_should_return_expected_result_when_coins_25() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_expected_result_with_all_values() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_return_expected_result_when_big_number_of_coins() -> None:
    assert get_coin_combination(1111116) == [1, 1, 1, 44444]
