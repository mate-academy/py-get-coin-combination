from app.main import get_coin_combination


def test_get_coin_combination_should_return_zeros() -> None:
    assert (
        get_coin_combination(0) == [0, 0, 0, 0]
    ), "test should return zeros when zero"


def test_get_coin_combination_should_return_ones() -> None:
    assert (
        get_coin_combination(41) == [1, 1, 1, 1]
    ), "test should return list of 1"


def test_get_coin_combination_should_return_quarters() -> None:
    assert (
        get_coin_combination(100) == [0, 0, 0, 4]
    ), "test should return four quarters"
