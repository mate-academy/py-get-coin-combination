from app.main import get_coin_combination


class TestGetCoinCombination:
    """Test cases for get_coin_combination function."""

    def test_zero_cents(self) -> None:
        """Test with 0 cents - should return all zeros."""
        assert get_coin_combination(0) == [0, 0, 0, 0]

    def test_single_penny(self) -> None:
        """Test with 1 cent - should return 1 penny."""
        assert get_coin_combination(1) == [1, 0, 0, 0]

    def test_multiple_pennies(self) -> None:
        """Test with 4 cents - should return 4 pennies."""
        assert get_coin_combination(4) == [4, 0, 0, 0]

    def test_single_nickel(self) -> None:
        """Test with 5 cents - should return 1 nickel."""
        assert get_coin_combination(5) == [0, 1, 0, 0]

    def test_penny_and_nickel(self) -> None:
        """Test with 6 cents - should return 1 penny + 1 nickel."""
        assert get_coin_combination(6) == [1, 1, 0, 0]

    def test_multiple_nickels(self) -> None:
        """Test with 9 cents - should return 4 pennies + 1 nickel."""
        assert get_coin_combination(9) == [4, 1, 0, 0]

    def test_single_dime(self) -> None:
        """Test with 10 cents - should return 1 dime."""
        assert get_coin_combination(10) == [0, 0, 1, 0]

    def test_dime_and_pennies(self) -> None:
        """Test with 13 cents - should return 3 pennies + 1 dime."""
        assert get_coin_combination(13) == [3, 0, 1, 0]

    def test_dime_and_nickel(self) -> None:
        """Test with 15 cents - should return 1 nickel + 1 dime."""
        assert get_coin_combination(15) == [0, 1, 1, 0]

    def test_complex_combination(self) -> None:
        """Test with 17 cents."""
        assert get_coin_combination(17) == [2, 1, 1, 0]

    def test_two_dimes(self) -> None:
        """Test with 20 cents - should return 2 dimes."""
        assert get_coin_combination(20) == [0, 0, 2, 0]

    def test_single_quarter(self) -> None:
        """Test with 25 cents - should return 1 quarter."""
        assert get_coin_combination(25) == [0, 0, 0, 1]

    def test_quarter_and_penny(self) -> None:
        """Test with 26 cents - should return 1 penny + 1 quarter."""
        assert get_coin_combination(26) == [1, 0, 0, 1]

    def test_quarter_and_nickel(self) -> None:
        """Test with 30 cents - should return 1 nickel + 1 quarter."""
        assert get_coin_combination(30) == [0, 1, 0, 1]

    def test_quarter_and_dime(self) -> None:
        """Test with 35 cents - should return 1 dime + 1 quarter."""
        assert get_coin_combination(35) == [0, 0, 1, 1]

    def test_all_coin_types(self) -> None:
        """Test with 41 cents - should use all coin types."""
        assert get_coin_combination(41) == [1, 1, 1, 1]

    def test_two_quarters(self) -> None:
        """Test with 50 cents - should return 2 quarters."""
        assert get_coin_combination(50) == [0, 0, 0, 2]

    def test_three_quarters(self) -> None:
        """Test with 75 cents - should return 3 quarters."""
        assert get_coin_combination(75) == [0, 0, 0, 3]

    def test_one_dollar(self) -> None:
        """Test with 100 cents - should return 4 quarters."""
        assert get_coin_combination(100) == [0, 0, 0, 4]

    def test_large_amount(self) -> None:
        """Test with 99 cents."""
        assert get_coin_combination(99) == [4, 0, 2, 3]

    def test_larger_amount(self) -> None:
        """Test with 140 cents."""
        assert get_coin_combination(140) == [0, 1, 1, 5]

    def test_very_large_amount(self) -> None:
        """Test with 1000 cents - should return 40 quarters."""
        assert get_coin_combination(1000) == [0, 0, 0, 40]

    def test_return_type(self) -> None:
        """Test that function returns a list."""
        result = get_coin_combination(10)
        assert isinstance(result, list)

    def test_return_length(self) -> None:
        """Test that function returns a list of length 4."""
        result = get_coin_combination(42)
        assert len(result) == 4

    def test_all_non_negative(self) -> None:
        """Test that all coin counts are non-negative."""
        result = get_coin_combination(87)
        assert all(count >= 0 for count in result)

    def test_correct_total_value(self) -> None:
        """Test that coin combination adds up to original amount."""
        cents = 67
        result = get_coin_combination(cents)
        total = (result[0] * 1 + result[1] * 5 + result[2] * 10
                 + result[3] * 25)
        assert total == cents
