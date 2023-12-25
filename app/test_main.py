from app.main import get_coin_combination


def test_one_cent() -> None:
    assert (
        get_coin_combination(1) == [1, 0, 0, 0]
    ), "Should return 1 penny for 1 cent"


def test_more_than_five_cents() -> None:
    assert (
        get_coin_combination(6) == [1, 1, 0, 0]
    ), "Should return 1 penny and 1 nickel for 6 cent's"


def test_more_than_15_cents() -> None:
    assert (
        get_coin_combination(17) == [2, 1, 1, 0]
    ), "Should return 2 penny 1 nickel and 1 dime for 17 cent"


def test_50_cents() -> None:
    assert (
        get_coin_combination(50) == [0, 0, 0, 2]
    ), "Should return 2 quarters for 50 cent"
