import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin, amount_in_cent",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "should return a list of zero",
        "should correctly return amount of penny",
        "should correctly return amount of penny and nickel",
        "amount of pennies, nickels and dimes must be correct",
        "correct amount to one coin of each type",
        "should correctly return amount of quarters"
    ]
)
def test_correct_type_of_each_coin(coin: int, amount_in_cent: list) -> None:
    assert (get_coin_combination(coin) == amount_in_cent)


def test_check_correct_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")
