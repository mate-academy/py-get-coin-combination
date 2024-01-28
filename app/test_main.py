import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount_cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_coin_combination_matches(
        amount_cents: int,
        result: list
) -> None:
    assert get_coin_combination(amount_cents) == result
