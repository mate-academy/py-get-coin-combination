import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="should return [0, 0, 0, 0]"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="should return [1, 0, 0, 0]"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="should return [0, 1, 0, 0]"
            ),
            pytest.param(
                10, [0, 0, 1, 0],
                id="should return [0, 0, 1, 0]"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="should return [0, 0, 0, 1]"
            ),
            pytest.param(
                41, [1, 1, 1, 1],
                id="should return [1, 1, 1, 1]"
            )
        ]
    )
    def test_main_function(
            self,
            cents: int,
            expected: list
    ) -> None:
        assert get_coin_combination(cents) == expected
