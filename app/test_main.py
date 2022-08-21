from app.main import get_coin_combination


def test_should_return_list():
    goals = get_coin_combination(75)

    assert isinstance(goals, list)


def test_should_return_list_of_given_length():
    goals = get_coin_combination(100)

    assert len(goals) == 4


def test_return_only_one_type():
    goals = get_coin_combination(41)

    assert goals == [1, 1, 1, 1]
