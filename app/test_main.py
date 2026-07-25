import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (75, [0, 0, 0, 3]),
        (80, [0, 1, 0, 3]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination(
    amount: int,
    expected: list[int]
) -> None:
    assert get_coin_combination(amount) == expected
