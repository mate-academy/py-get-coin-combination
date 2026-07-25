import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (55, [0, 1, 0, 2]),
        (67, [2, 1, 1, 2]),
        (1234567, [2, 1, 1, 49382])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected, (
        f"Error: {get_coin_combination(cents)} != {expected}"
    )
