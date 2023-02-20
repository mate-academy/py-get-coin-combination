import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3])
    ]
)
def test_different_coin_combinations(cents: int, expected: list) -> None:
    assert (
        get_coin_combination(cents) == expected
    ), f"{cents} cents should return {expected} combination"
