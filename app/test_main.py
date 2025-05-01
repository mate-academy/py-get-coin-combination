from app.main import get_coin_combination


def test_get_coin_combination_1() -> None:
    result = [1, 0, 0, 0]
    result_code = get_coin_combination(1)
    assert result == result_code


def test_get_coin_combination_2() -> None:
    result = [1, 1, 0, 0]
    result_code = get_coin_combination(6)
    assert result == result_code


def test_get_coin_combination_3() -> None:
    result = [2, 1, 1, 0]
    result_code = get_coin_combination(17)
    assert result == result_code


def test_get_coin_combination_4() -> None:
    result = [0, 0, 0, 2]
    result_code = get_coin_combination(50)
    assert result == result_code
