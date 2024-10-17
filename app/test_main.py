from app.main import get_coin_combination


def test_parameter_equal_zero() -> None:
    assert (get_coin_combination(0) == [0, 0, 0, 0])


def test_parameter_equal_to_one() -> None:
    assert (get_coin_combination(1) == [1, 0, 0, 0])


def test_float_value_of_parameter() -> None:
    assert (get_coin_combination(23.2) == [3.0, 0.0, 2.0, 0.0])


def test_very_big_value_of_parameter() -> None:
    assert (get_coin_combination(123445) == [0, 0, 2, 4937])


def test_primal_value_of_parameter() -> None:
    assert (get_coin_combination(47) == [2, 0, 2, 1])


def test_normal_value_of_parameter() -> None:
    assert (get_coin_combination(75) == [0, 0, 0, 3])
