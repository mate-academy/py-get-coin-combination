from app.main import get_coin_combination


def test_should_return_list():
    goals = get_coin_combination(5)
    assert isinstance(goals, list)

def test_should_return_list_length_must_be_four():
    goals = get_coin_combination(30)
    assert len(goals) == 4

def test_should_return_expected_goals_when_value_is_one():
    goals = get_coin_combination(1)
    assert goals == [1, 0, 0, 0]

def test_should_return_expected_goals_when_value_is_six():
    goals = get_coin_combination(6)
    assert goals == [1, 1, 0, 0]

def test_should_return_expected_goals_when_value_is_seventeen():
    goals = get_coin_combination(17)
    assert goals == [2, 1, 1, 0]

def test_should_return_expected_goals_when_value_is_fifty():
    goals = get_coin_combination(50)
    assert goals == [0, 0, 0, 2]