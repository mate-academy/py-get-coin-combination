import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, results",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (87, [2, 0, 1, 3]),
        (41, [1, 1, 1, 1]),
    ]
)
def test_get_coin_combination(cents: int, results: list) -> None:
    assert (
        get_coin_combination(cents) == results
    ), f"For {cents} cents should be {results} number of coins"
