import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, penny, nickel, dime, quarters",
    [
        (1, 1, 0, 0, 0),
        (6, 1, 1, 0, 0),
        (17, 2, 1, 1, 0),
        (50, 0, 0, 0, 2),
    ],
    ids=[
        "test for 1 penny.",
        "test for 1 penny and 1 nickel.",
        "test for 2 penny, 1 nickel, 1 dime.",
        "test for 2 quarters.",
    ]
)
def test_output_result(
        coins: int, penny: int,
        nickel: int, dime: int, quarters: int
    ) -> None:
    assert get_coin_combination(coins) == [penny, nickel, dime, quarters]
