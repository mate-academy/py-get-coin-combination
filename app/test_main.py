import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(0, [0, 0, 0, 0],
                     id="test should return zeroes if zero coins"),
        pytest.param(1, [1, 0, 0, 0],
                     id="test should return order of coins: "
                        "[1 cent, 5 cents, 10 cents, 25 cents]"),
        pytest.param(17, [2, 1, 1, 0],
                     id="test should return zero quarters if "
                        "amount of cents less than 25"),
        pytest.param(100, [0, 0, 0, 4],
                     id="test should return only quarters if "
                        "cents are divisible by 25"),
        pytest.param(0, [0, 0, 0, 0],
                     id="test may return different results "
                        "for different animals"),
        pytest.param(1234, [4, 1, 0, 49],
                     id="test should work with lots of coins")
    ]
)
def test_correct_human_age(
        cents: int,
        coins: int
) -> None:
    assert (get_coin_combination(cents) == coins), \
        (f"The smallest possible number of {cents} coins "
         f"should be equal to {coins}.")
