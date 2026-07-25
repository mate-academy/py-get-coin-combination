from app.main import get_coin_combination


def test_list() -> None:
    result = get_coin_combination(2)
    assert isinstance(result, list)


def test_one_penny() -> None:
    result = get_coin_combination(2)
    assert result == [2, 0, 0, 0]


def test_nickel() -> None:
    result = get_coin_combination(7)
    assert result == [2, 1, 0, 0]


def test_dimes() -> None:
    result = get_coin_combination(19)
    assert result == [4, 1, 1, 0]


def test_quarter() -> None:
    result = get_coin_combination(27)
    assert result == [2, 0, 0, 1]
