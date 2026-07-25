from app.main import get_coin_combination


def test_should_check_work_with_penny_nickel_dime() -> None:
    assert (
        get_coin_combination(17) == [2, 1, 1, 0]
    ), ("should check work with penny, nickel,"
        " dime and calculate smallest possible"
        " number of coins (17) == [2, 1, 1, 0]")


def test_should_check_work_with_quarters_smallest_numbers_of_coins() -> None:
    assert (
        get_coin_combination(50) == [0, 0, 0, 2]   # 2 quarters
    ), ("should check work with quarters and calculate smallest possible"
        " number of coins (50) == [0, 0, 0, 2]")
