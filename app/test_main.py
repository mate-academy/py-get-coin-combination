from app.main import get_coin_combination


# write your tests here
def test_get_coin_combination_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_99() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_coin_combination_100() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_get_coin_combination_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_3() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_get_coin_combination_11() -> None:
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_get_coin_combination_24() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]
