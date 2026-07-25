import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coin_combination", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0 , 1]),
        (30, [0, 1, 0, 1]),
        (48, [3, 0, 2, 1]),
        (70, [0, 0, 2, 2]),
    ]
)
def test_some_combinations(
    cents: int,
    coin_combination: list
) -> None:
    assert get_coin_combination(cents) == coin_combination
