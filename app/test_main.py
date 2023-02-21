from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(99) == [4, 0, 2, 3]

