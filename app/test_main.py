from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (23, [3, 0, 2, 0]),
        (35, [0, 0, 1, 1]),
        (50, [0, 0, 0, 2])
    ],
    ids=(
        "checks 1 cent",
        "checks 23 cents",
        "checks 35 cents",
        "checks 50 cents"
    )
)
def test_give_us_amount_of_coind_in_cent(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result
