from app.main import get_coin_combination


def test_get_coin_combination_should_return_list() -> None:
    assert isinstance(get_coin_combination(0), list)


def test_get_coin_combination_should_return_a_list_with_four_values() -> None:
    assert len(get_coin_combination(0)) == 4


def test_get_coin_combination_if_coin_equal_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_gry_coin_combination_should_counting_starting_from_the_end() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_should_count_all_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]
