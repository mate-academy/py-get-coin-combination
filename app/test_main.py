import pytest
import app.main


@pytest.mark.parametrize(
    "cents,expected",
    [
        # Граничні умови для нуля
        (0, [0, 0, 0, 0]),

        # Межі номіналу Pennies (1-4 центи)
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),

        # Межа переходу на Nickels (5 центів)
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),

        # Межа переходу на Dimes (10 центів)
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),

        # Межа переходу на Quarters (25 центів)
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),

        # Великі значення суми
        (100, [0, 0, 0, 4]),
    ]
)
def test_get_coin_combination_boundaries(
    cents: int,
    expected: list[int]
) -> None:
    """Перевірка граничних значень комбінацій монет."""
    assert app.main.get_coin_combination(cents) == expected
