import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            (0, [0, 0, 0, 0]),          # zero input — should return no coins
            (1, [1, 0, 0, 0]),          # single penny
            (2, [2, 0, 0, 0]),
            (4, [4, 0, 0, 0]),          # max pennies before first nickel
            (5, [0, 1, 0, 0]),          # exactly one nickel
            (6, [1, 1, 0, 0]),          # penny + nickel
            (10, [0, 0, 1, 0]),         # exactly one dime
            (11, [1, 0, 1, 0]),         # penny + dime
            (15, [0, 1, 1, 0]),         # nickel + dime
            (17, [2, 1, 1, 0]),         # 2 pennies + nickel + dime
            (25, [0, 0, 0, 1]),         # exactly one quarter
            (26, [1, 0, 0, 1]),         # penny + quarter
            (30, [0, 1, 0, 1]),         # nickel + quarter
            (35, [1, 1, 0, 1]),         # penny + nickel + quarter
            (41, [1, 1, 1, 1]),         # one of each coin
            (99, [4, 0, 2, 3]),         # complex combination
            (1234, [4, 1, 0, 49])       # large value — stress test
        ]
    )
    def test_should_return_expected_combination_for_valid_inputs(
        self, cents: int, expected: list[int]
    ) -> None:
        result = get_coin_combination(cents)
        assert result == expected, (
            f"For {cents} cents expected {expected}, got {result}"
        )

    def test_should_return_list_of_four_integers(self) -> None:
        result = get_coin_combination(17)

        assert isinstance(result, list), "Result should be a list"
        assert len(result) == 4, "Result list should have 4 elements"
        assert all(isinstance(x, int) for x in result), (
            "All elements should be integers"
        )

    @pytest.mark.parametrize("cents", [0, 1, 17, 41, 99, 1234])
    def test_should_return_combination_that_matches_input_sum(
        self, cents: int
    ) -> None:
        result = get_coin_combination(cents)
        total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25

        assert total == cents, (
            f"Returned coins {result} do not sum to {cents} cents"
        )
