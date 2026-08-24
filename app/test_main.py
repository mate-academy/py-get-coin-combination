import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (24, [4, 0, 2, 0]),
        (67, [2, 1, 1, 2])
    ]
)
def test_coin_combinations(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
