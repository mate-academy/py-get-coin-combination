import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "initial_cent, expected_value",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="should return 0 when number of cent 0"
            ),

            pytest.param(
                1, [1, 0, 0, 0],
                id="should return 1 penny when number of cent 1 penny"
            ),

            pytest.param(
                6, [1, 1, 0, 0],
                id="should return 1 nickel when number of cent 1 nickel"
            ),

            pytest.param(
                17, [2, 1, 1, 0],
                id="should return 1 dime when number of cent 1 dime"
            ),

            pytest.param(
                25, [0, 0, 0, 1],
                id="shoould return 1 quaters when number of cent 1 quater"
            )
        ]
    )
    def test_returns_correct_result(
        self,
        initial_cent: int,
        expected_value: list
    ) -> None:
        assert get_coin_combination(initial_cent) == expected_value


class TestRaiseGetCoinCombination:

    @pytest.mark.parametrize(
        "initial_cent",
        [
            pytest.param("1", id="type of attribute should be int or float"),
            pytest.param([1], id="type of attribute should be int or float")
        ]
    )
    def tests_raise_typeerror(
        self,
        initial_cent: int
    ) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(initial_cent)
