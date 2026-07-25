from app.main import get_coin_combination


# write your tests here
def test_coin_comination_coin_value_zero() -> None:
    expected = get_coin_combination(0)
    assert expected == [0, 0, 0, 0]


def test_coin_comination_with_different_types() -> None:
    expected = get_coin_combination(25)
    result = [0, 0, 0, 1]
    assert expected == result


def test_coin_combination_different_coins() -> None:
    expected = get_coin_combination(9)
    result = [4, 1, 0, 0]
    assert expected == result
