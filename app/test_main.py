import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "1 cent = 1 penny",
        "17 cents = 2 pennies + 1 nickel + 1 dime",
        "50 cents = 2 quarters"
    ]
)
def test_is_correct_for_different_cents_given(
        cents: int,
        result: list
) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"Combination of {cents} cent/cents should be equal to {result}"
