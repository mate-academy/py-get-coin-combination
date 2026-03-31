import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins_number",
    [
        (25, [0, 0, 0, 1]),
        (48, [3, 0, 2, 1]),
        (75, [0, 0, 0, 3]),
        (8, [3, 1, 0, 0]),
        (53, [3, 0, 0, 2])
    ]
)
def test_get_coin_combination(cents: int,
                              coins_number: list) -> None:
    assert get_coin_combination(cents) == coins_number
