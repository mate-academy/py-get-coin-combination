import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (20, [0, 0, 2, 0]),
        (50, [0, 0, 0, 2]),
        (83, [3, 1, 0, 3])
    ]
)
def test_cents_to_currency(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result
