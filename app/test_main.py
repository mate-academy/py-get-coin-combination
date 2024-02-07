import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_coin_combination",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="1 cent should return [1, 0, 0, 0]"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="17 cent should return [2, 1, 1, 0]"
            ),
        ]
    )
    def test_for_expected_result(
            self,
            cents: int,
            expected_coin_combination: [int],
    ) -> None:

        assert get_coin_combination(cents) == expected_coin_combination
