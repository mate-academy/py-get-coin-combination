import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",[
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (-5, [0, 0, 2, -1]),
        (3.5, [3.0, 0.0, 0.0, 0.0]),
        (10000, [0, 0, 0, 400]),
    ]
)

def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
