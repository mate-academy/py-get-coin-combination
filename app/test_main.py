import pytest
from app.main import get_coin_combination


class TestGetCoinCombination():
    @pytest.mark.parametrize(
        "cents,results",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Check with 1 cent"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Check with 6 cents"
            ),
            pytest.param(
                16,
                [1, 1, 1, 0],
                id="Check with 16 cents"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="Check with 41 cents"
            ),
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            results: list
    ) -> None:
        assert get_coin_combination(cents) == results
