import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "input_cents,output_combination",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="Should return zero for zero cents"
            ),
            pytest.param(
                4, [4, 0, 0, 0],
                id="Should return only pennies when `cents` < 5"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="Should return only 1 nickel when `cents` = 5"
            ),
            pytest.param(
                20, [0, 0, 2, 0],
                id="Should return only dimes"
                #
            ),
            pytest.param(
                75, [0, 0, 0, 3],
                id="Should return only quarters"
                #
            ),
            pytest.param(
                93, [3, 1, 1, 3],
                id="Should return correctly mixed coin combination"
                #
            ),
            pytest.param(
                569, [4, 1, 1, 22],
                id="Should return correct combination for large amounts"
                #
            )
        ]
    )
    def test_calculate_coin_combination_correctly(self,
                                                  input_cents: int,
                                                  output_combination: list
                                                  ) -> None:
        assert get_coin_combination(input_cents) == output_combination
