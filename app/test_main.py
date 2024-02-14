from app.main import get_coin_combination


def test_for_result_one_penny() -> None:
    assert (get_coin_combination(1) == [1, 0, 0, 0])


def test_for_result_one_penny_and_one_nickel() -> None:
    assert (get_coin_combination(6) == [1, 1, 0, 0])


def test_for_result_two_pennies_one_nickel_and_one_dime() -> None:
    assert (get_coin_combination(17) == [2, 1, 1, 0])


def test_for_two_quarters() -> None:
    assert (get_coin_combination(50) == [0, 0, 0, 2])
