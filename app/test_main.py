from app.main import get_coin_combination


def test_coin_combinationn_1() -> None:
    assert (
        get_coin_combination(50) == [0, 0, 0, 2]
    ), "could return different coins, not only pennies"


def test_coin_combinationn_2() -> None:
    assert (
        get_coin_combination(17) == [2, 1, 1, 0]
    ), "could return coins of the different types"
