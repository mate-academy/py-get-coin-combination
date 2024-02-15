import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "pennies,cents",
    [
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_correct_combination(pennies: int, cents: list) -> None:
    assert get_coin_combination(pennies) == cents