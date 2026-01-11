import pytest

from app.main import get_coin_combination


class TestResults:
    @pytest.mark.parametrize(
        "input_value,expected_result",
        [
            pytest.param(1, [1, 0, 0, 0],
                         id="should return  one penny"),
            pytest.param(6, [1, 1, 0, 0],
                         id="should return  one penny + one nickel"),
            pytest.param(17, [2, 1, 1, 0],
                         id="should return two penny + one nickel + one dime"),
            pytest.param(50, [0, 0, 0, 2],
                         id="value should return 2 quarters")
        ]
    )
    def test_program_counts_correctly(self,
                                      input_value: int,
                                      expected_result: list) -> None:
        result = get_coin_combination(input_value)
        assert result == expected_result
