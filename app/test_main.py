import pytest
from app.main import get_coin_combination  # Ensure correct import


@pytest.mark.parametrize(
    "cents, expected_options",
    [
        (1, [[1, 0, 0, 0]]),  # Only pennies
        (5, [[0, 1, 0, 0]]),  # Only nickels
        (10, [[0, 0, 1, 0]]),  # Only dimes
        (25, [[0, 0, 0, 1]]),  # Only quarters
        (30, [[0, 0, 3, 0], [0, 1, 0, 1]]),  # 3 dimes OR 1 quarter + 1 nickel
        (99, [[4, 0, 2, 3]])  # Mixed case
    ],
)
def test_various_cases(cents: int, expected_options: list[list[int]]) -> None:
    """Ensure get_coin_combination handles various cases correctly."""
    assert get_coin_combination(cents) in expected_options, (
        f"Unexpected result for {cents} cents"
    )
