import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "integer, result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (40, [0, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (70, [0, 0, 2, 2]),
    ],
    ids=[
        "1 should result in [1, 0, 0, 0]",
        "5 should result in [0, 1, 0, 0]",
        "10 should result in [0, 0, 1, 0]",
        "25 should result in [0, 0, 0, 1]",
        "40 should result in [0, 1, 1, 1]",
        "50 should result in [0, 0, 0, 2]",
        "70 should result in [0, 0, 2, 2]",
    ]
)
def test_get_coin_combination(integer: int, result: list) -> None:
    assert get_coin_combination(integer) == result
