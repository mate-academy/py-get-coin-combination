from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents_to_calculate, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1])

    ]
)
def test_get_coin_combinations(cents_to_calculate: int,
                               expected: int) -> None:
    assert get_coin_combination(cents_to_calculate) == expected
