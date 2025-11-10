import pytest
from app.main import get_coin_combination


class TestBasicLogic:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (6, [1, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (15, [0, 1, 1, 0]),
            (17, [2, 1, 1, 0]),
            (24, [4, 0, 2, 0]),
            (25, [0, 0, 0, 1]),
            (30, [0, 1, 0, 1]),
            (40, [0, 1, 1, 1]),
            (50, [0, 0, 0, 2]),
            (99, [4, 0, 2, 3]),
        ]
    )
    def test_should_return_min_number_of_coins(self,
                                               cents: int,
                                               expected: list[int]) -> None:
        assert get_coin_combination(cents) == expected


class TestStructure:
    def test_should_return_list_of_four_numbers(self) -> None:
        result = get_coin_combination(10)
        assert isinstance(result, list)
        assert len(result) == 4

    def test_all_values_should_be_integers(self) -> None:
        result = get_coin_combination(10)
        assert all(isinstance(x, int) for x in result)

    def test_all_values_should_be_non_negative(self) -> None:
        result = get_coin_combination(10)
        assert all(x >= 0 for x in result)


class TestCorrectness:
    @pytest.mark.parametrize("cents", [0, 7, 18, 33, 68, 123])
    def test_sum_of_coins_equals_input_amount(self, cents: int) -> None:
        pennies, nickels, dimes, quarters = get_coin_combination(cents)
        total = pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25
        assert total == cents


class TestGreedyOptimality:
    @pytest.mark.parametrize(
        "cents",
        [25, 30, 31, 37, 41, 55, 89]
    )
    def test_should_use_quarters_first(self, cents: int) -> None:
        result = get_coin_combination(cents)
        if cents >= 25:
            assert result[3] == cents // 25
