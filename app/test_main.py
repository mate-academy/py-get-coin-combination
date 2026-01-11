from app.main import get_coin_combination


def test_on_return_type() -> None:
    result = get_coin_combination(50)
    assert isinstance(result, list)


def test_on_result_len() -> None:
    result = get_coin_combination(20)
    assert len(result) == 4


def test_on_one_type_coin() -> None:
    result = get_coin_combination(75)
    assert result == [0, 0, 0, 3]


def test_on_different_type_coins() -> None:
    result = get_coin_combination(17)
    assert result == [2, 1, 1, 0]
