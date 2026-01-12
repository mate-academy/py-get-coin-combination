from app.main import get_coin_combination
from pytest import mark


@mark.parametrize(
    "coin,pennies,nickel,dime,quarters",
    [
        (1, 1, 0, 0, 0),
        (6, 1, 1, 0, 0),
        (17, 2, 1, 1, 0),
        (50, 0, 0, 0, 2)
    ]
)
def test_get_coin_combination(coin: int,
                              pennies: int,
                              nickel: int,
                              dime: int,
                              quarters: int) -> None:

    assert get_coin_combination(coin) == [pennies,
                                          nickel,
                                          dime,
                                          quarters]
