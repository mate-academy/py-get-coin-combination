from app.main import get_coin_combination


def get_coin_combination_list() -> None:
    goals = get_coin_combination(0)
    assert isinstance(goals, list)


def test_should_return_list_of_given_length() -> None:
    goals = get_coin_combination(0)
    assert len(goals) == 4


def test_should_return_1_penny_then_given_1_cents() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_1_penny_1_nickel_then_given_6_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_2_penny_1_nickel_1_dime_then_given_17_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_2_quarters_then_given_50_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
