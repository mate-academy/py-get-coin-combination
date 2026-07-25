from app.main import get_coin_combination


def test_should_return_different_coins() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_should_return_different_combinations() -> None:
    assert get_coin_combination(2) == [2, 0, 0, 0]
    assert get_coin_combination(7) == [2, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(44) == [4, 1, 1, 1]
