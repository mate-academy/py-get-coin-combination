from typing import List

import pytest
from app.main import get_coin_combination


class TestParameterizedCasesGetCoinCombination:
    """Parameterized tests for multiple cases with descriptive IDs."""

    @pytest.mark.parametrize("cents, expected", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (16, [1, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (21, [1, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (31, [1, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (40, [0, 1, 1, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (119, [4, 1, 1, 4]),
    ], ids=[
        "zero_cents",
        "one_cent_penny_only",
        "four_pennies",
        "exact_nickel",
        "penny_and_nickel",
        "four_pennies_and_nickel",
        "exact_dime",
        "dime_and_penny",
        "three_nickels",
        "three_nickels_and_penny",
        "example_17_cents",
        "two_dimes",
        "two_dimes_and_penny",
        "exact_quarter",
        "quarter_and_penny",
        "quarter_and_nickel",
        "quarter_nickel_and_penny",
        "quarter_and_two_nickels",
        "quarter_and_three_nickels",
        "all_coin_types_41_cents",
        "two_quarters",
        "large_amount_99_cents",
        "four_quarters",
        "complex_119_cents",
    ])
    def test_various_amounts(self, cents: int, expected: List[int]) -> None:
        """Test various amounts with parameterized inputs."""
        result = get_coin_combination(cents)
        assert result == expected, (f"Failed for {cents} cents. "
                                    f"Expected {expected}, got {result}")


class TestRaiseErrorsGetCoinCombination:

    def test_incorrect_data_types(self) -> None:
        """Test that incorrect data types raise TypeError"""
        # Test with string
        with pytest.raises(TypeError):
            get_coin_combination("15")

        # Test with None
        with pytest.raises(TypeError):
            get_coin_combination(None)

        # Test with list
        with pytest.raises(TypeError):
            get_coin_combination([15])
