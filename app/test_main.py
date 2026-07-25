from app.main import get_coin_combination
import pytest


# write your tests here
@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (25, [0, 0, 0, 1]),
        (11, [1, 0, 1, 0]),
        (30, [0, 1, 0, 1])
    ]
)
def test_correct_coin_combination(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result
