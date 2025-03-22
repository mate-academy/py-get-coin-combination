import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (2, [2, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (6, [1, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (11, [1, 0, 1, 0]),
            (15, [0, 1, 1, 0]),
            (17, [2, 1, 1, 0]),
            (25, [0, 0, 0, 1]),
            (26, [1, 0, 0, 1]),
            (30, [0, 1, 0, 1]),
            (35, [1, 1, 0, 1]),
            (41, [1, 1, 1, 1]),
            (99, [4, 0, 2, 3]),
            (1234, [4, 1, 0, 49])
        ]
    )
    def test_should_return_expected_combination_for_valid_inputs(
        self, cents, expected
    ) -> None:
        result = get_coin_combination(cents)
        assert result == expected, (
            f"For {cents} cents expected {expected}, got {result}"
        )

    def test_should_return_list_of_four_integers(self) -> None:
        result = get_coin_combination(17)
        assert isinstance(result, list)
        assert len(result) == 4
        assert all(isinstance(x, int) for x in result)

    @pytest.mark.parametrize("cents", [0, 1, 17, 41, 99, 1234])
    def test_should_return_combination_that_matches_input_sum(
        self, cents
    ) -> None:
        result = get_coin_combination(cents)
        total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
        assert total == cents
