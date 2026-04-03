from app.main import get_coin_combination


def test_shold_return_four_elements_list() -> None:
    assert len(get_coin_combination(0)) == 4


def test_should_return_equals_sum() -> None:
    result = get_coin_combination(57)
    assert result[0] + result[1] * 5 + result[2] * 10 + result[3] * 25 == 57


def test_should_returns_minimum_coins() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
