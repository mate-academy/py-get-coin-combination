import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "0 cents should be equal to 0 coins",
        "amount of coins that equal to 1 cent",
        "amount of coins that equal to 6 cents",
        "amount of coins that equal to 17 cents",
        "amount of coins that equal to 50 cents"
    ]
)
def test_check_correct_coins_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result

def sum_of_coins_must_be_equal_to_cents() -> None:
    assert (get_coin_combination(50)[0] + get_coin_combination(50)[1] * 5
    + get_coin_combination(50)[2] * 10 + get_coin_combination(50)[3] * 25) == 50

def amount_of_cents_should_be_not_less_than_0() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)