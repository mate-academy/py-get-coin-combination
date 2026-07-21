from app.main import get_coin_combination


# write your tests here
def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_coin() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fifty() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]
