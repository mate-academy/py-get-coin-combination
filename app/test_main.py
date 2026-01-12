import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "input_value,expected_value",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="Must work with zero value"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Must work with minimal value"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="Must work with minimal value"
            )
        ]
    )
    def test_correctly_worked(self,
                              input_value: int,
                              expected_value: list[int]) -> None:
        assert get_coin_combination(input_value) == expected_value
