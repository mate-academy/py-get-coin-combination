from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cent, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (141, [1, 1, 1, 5]),
        (201, [1, 0, 0, 8])
    ],
    ids=[
        "0 cent",
        "1 cent",
        "6 cent",
        "17 cent",
        "41 cent",
        "50 cent",
        "141 cent",
        "201 cent"
    ]
)
def test_get_coin_combination_positive(cent: int, expected: list[int]) -> None:
    assert get_coin_combination(cent) == expected
