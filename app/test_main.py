import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 cent",
        "6 cents",
        "17 cents",
        "50 cents"
    ]
)
def test_can_combinate_coins(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result, f"Result should be {result}"
