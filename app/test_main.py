from app.main import get_coin_combination


def test_check_type_of_function() -> None:
    assert isinstance(get_coin_combination(50), list)


def test_check_right_values_() -> None:
    assert len(get_coin_combination(1)) == 4


def test_check_right_values_type() -> None:
    assert isinstance(get_coin_combination(1123)[1], int)


def test_check_right_values_from_small_to_big() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_check_values_in_non_normal_range() -> None:
    assert get_coin_combination(500) == [0, 0, 0, 20]
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(1424142) == [2, 1, 1, 56965]
