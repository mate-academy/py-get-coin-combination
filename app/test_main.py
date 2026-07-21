from app.main import get_coin_combination


def test_should_return_min_coins() -> None:
    assert sum(get_coin_combination(25)) == 1


def test_should_return_all_1() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_should_return_all_zeros() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
