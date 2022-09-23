import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_list",
        [pytest.param(
            1,
            [1, 0, 0, 0],
            id="Should return list"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="Should return list"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="Should return list"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="Should return list"
        )]
    )
    def test_should_return_expected_list(
            self,
            cents,
            expected_list):
        assert get_coin_combination(cents) == expected_list
