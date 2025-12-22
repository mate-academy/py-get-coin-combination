import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(amount: int, expected: list) -> None:
    assert get_coin_combination(amount) == expected

def test_negative_amount_raises_value_error() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)