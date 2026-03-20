import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "inputs, expected",
        [
            pytest.param(1, [1, 0, 0, 0], id="1 penny"),
            pytest.param(6, [1, 1, 0, 0], id="1 penny, 1 nickel"),
            pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
            pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
            pytest.param(0, [0, 0, 0, 0], id="zero cents"),
            pytest.param(99, [4, 0, 2, 3], id="complex case 99 cents")
        ]
    )
    def test_number_of_cent(
            self,
            inputs: int,
            expected: list[int]
    ) -> None:
        result = get_coin_combination(inputs)
        assert result == expected
