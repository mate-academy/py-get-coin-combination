from app.main import get_coin_combination


def test_should_return_one_penny_for_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_nickel_and_one_penny_for_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_correct_combination_for_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_two_quarters_for_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_empty_combination_for_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_smallest_possible_number_of_coins() -> None:
    result = get_coin_combination(30)
    assert result == [0, 1, 0, 1]
