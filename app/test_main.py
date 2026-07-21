from app.main import get_coin_combination

import pytest


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        ("cents", "result"),
        [
            pytest.param(1, [1, 0, 0, 0], id="1 penny"),
            pytest.param(7, [2, 1, 0, 0], id="2 penny and 1 nickel"),
            pytest.param(16, [1, 1, 1, 0], id="1 penny, 1 nickel and 1 dime"),
            pytest.param(55, [0, 1, 0, 2], id="1 nickel and 2 quarters"),
        ])
    def test_should_return_coin_combination(
            self,
            cents: int,
            result: list
    ) -> None:
        assert get_coin_combination(cents) == result
