import pytest


from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            pytest.param(
                1, [1, 0, 0, 0], id="Should return 1 penny when sum is 1"
            ),
            pytest.param(
                5, [0, 1, 0, 0], id="Should return 1 nickel when sum is 5"
            ),
            pytest.param(
                10, [0, 0, 1, 0], id="Should return 1 dime when sum is 10"
            ),
            pytest.param(
                25, [0, 0, 0, 1], id="Should return 1 quarter when sum is 10"
            ),
            pytest.param(
                67, [2, 1, 1, 2], id="Should return correct value"
            ),
            pytest.param(
                0, [0, 0, 0, 0], id="Should return 0 quarter when sum is 0"
            ),
        ]
    )
    def test_get_coin_combination_correctly(
            self,
            cents: int,
            expected_result: list) -> None:
        assert get_coin_combination(cents) == expected_result
