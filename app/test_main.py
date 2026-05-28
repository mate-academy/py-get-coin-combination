import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (19, [4, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
    ],
    ids=[
        "Coins when cents=0",
        "Coins when cents=1",
        "Coins when cents=4",
        "Coins when cents=5",
        "Coins when cents=9",
        "Coins when cents=10",
        "Coins when cents=19",
        "Coins when cents=25",
        "Coins when cents=41",
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
