import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "1 cents",
        "6 cents",
        "17 cents",
        "50 cents",
    ]
)
def test_get_coin_combination(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result, (
        f"The smallest combination for {cents} cents is {result}. "
    )
