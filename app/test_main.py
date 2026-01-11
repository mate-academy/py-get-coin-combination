from app.main import get_coin_combination


def test_should_return_smallest_combination_possible_number_of_coins() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]
