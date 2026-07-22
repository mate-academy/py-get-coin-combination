from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents,combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "cents=1 should return[1,0,0,0]",
        "cents=6 should return[1,1,0,0]",
        "cents=17 should return[2,1,1,0]",
        "cents=50 should return[0,0,0,2]",
    ]
)
def test_get_coin_combination(cents: int, combination: list) -> None:
    assert get_coin_combination(cents) == combination
