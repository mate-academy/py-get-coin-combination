from app.main import get_coin_combination

import pytest


class TestGetCoinCombinations:
    @pytest.mark.parametrize(
        "cents,coins",
        [
            pytest.param(17, [2, 1, 1, 0], id="should return correct results"),

        ]
    )
    def test_correct_results(
            self,
            cents: int,
            coins: list[int]
    ) -> None:
        assert get_coin_combination(cents) == coins

    @pytest.mark.parametrize(
        "cents,exception",
        [
            pytest.param("h", TypeError, id="coin type should be integer"),

        ]
    )
    def test_correct_exception(
            self,
            cents: int,
            exception: tuple
    ) -> None:
        with pytest.raises(expected_exception=exception):
            get_coin_combination(cents)
