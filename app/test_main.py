from app.main import get_coin_combination


def test1() -> None:
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0]


def test2() -> None:
    result = get_coin_combination(6)
    assert result == [1, 1, 0, 0]


def test3() -> None:
    result = get_coin_combination(17)
    assert result == [2, 1, 1, 0]


def test4() -> None:
    result = get_coin_combination(50)
    assert result == [0, 0, 0, 2]
