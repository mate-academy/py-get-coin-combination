import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1",
        "2",
        "3",
        "4"
    ],
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result, (
        f"Coin combination {cents} equal to {result}"
    )
