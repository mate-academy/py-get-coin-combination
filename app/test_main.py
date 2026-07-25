import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_coins_combinations(cents: int, expected_coins: list) -> None:
    assert (
        get_coin_combination(cents) == expected_coins
    ), f"For {cents} cents expected coin combination {expected_coins}"
