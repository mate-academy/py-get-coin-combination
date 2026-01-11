import pytest

from app.main import get_coin_combination


class TestCombines:
    @pytest.mark.parametrize(
        "cents, expected_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should returns all 0 list"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should returns all [1, 0, 0, 0]"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should returns all [1, 1, 0, 0]"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should returns all [2, 1, 1, 0]"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should returns all [0, 0, 0, 2]"
            ),
        ]
    )
    def test_some_non_negative_values_include_0(self, cents, expected_list):
        assert get_coin_combination(cents) == expected_list
