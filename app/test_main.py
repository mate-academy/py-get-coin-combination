import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (16, [1, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (106, [1, 1, 0, 4]),
    ]
)
def test_get_coin_combination(input_cents: int, result: list) -> None:
    assert get_coin_combination(input_cents) == result
