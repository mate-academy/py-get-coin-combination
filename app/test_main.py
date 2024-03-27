from app.main import get_coin_combination


def test_when_only_one_cent() -> None:
    assert (get_coin_combination(1) == [1, 0, 0, 0]
            ), "cent should be in zero indexes"


def test_when_cents_more_than_5() -> None:
    assert (get_coin_combination(6) == [1, 1, 0, 0]
            ), "1 penny + 1 nickel"


def test_entered_dimes() -> None:
    assert (get_coin_combination(17) == [2, 1, 1, 0]
            ), "2 pennies + 1 nickel + 1 dime"


def test_entered_two_quarters() -> None:
    assert (get_coin_combination(50) == [0, 0, 0, 2]
            ), "2 quarters"
