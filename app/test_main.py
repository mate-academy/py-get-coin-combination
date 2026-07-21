import pytest


from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "value, exp_result",
        [
            pytest.param(0, [0, 0, 0, 0],
                         id="Should return empty list when value is zero"),
            pytest.param(1, [1, 0, 0, 0],
                         id="Should return only one number in list"),
            pytest.param(6, [1, 1, 0, 0],
                         id="test six cents"),
            pytest.param(17, [2, 1, 1, 0],
                         id="test seventeen cents"),
            pytest.param(50, [0, 0, 0, 2],
                         id="test seventeen cents"),
        ]
    )
    def test_different_values(self, value: int, exp_result: list) -> None:
        assert get_coin_combination(value) == exp_result
