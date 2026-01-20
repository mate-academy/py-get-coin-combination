from app.main import get_coin_combination


def test_return_only_one_coin() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_two_type_of_coins() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_return_three_type_of_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_return_four_type_of_coins() -> None:
    assert get_coin_combination(67) == [2, 1, 1, 2]
