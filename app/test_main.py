from app.main import get_coin_combination


def test_should_return_one_type_of_coin() -> None:
    values = 10
    expected_result = [0, 0, 1, 0]
    result = get_coin_combination(values)
    assert result == expected_result


def test_should_return_different_type_of_coins() -> None:
    values = 17
    expected_result = [2, 1, 1, 0]
    result = get_coin_combination(values)
    assert result == expected_result


def test_should_return_zero_list() -> None:
    values = 0
    expected_result = [0, 0, 0, 0]
    result = get_coin_combination(values)
    assert result == expected_result
