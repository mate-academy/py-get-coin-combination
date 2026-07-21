import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should return [0, 0, 0, 0] when cents = 0"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return [1, 0, 0, 0] when cents = 1"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return [1, 1, 0, 0] when cents = 6"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return [2, 1, 1, 0] when cents = 17"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="should return [1, 1, 1, 1] when cents = 41"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return [0, 0, 0, 2] when cents = 50"
            ),
            pytest.param(
                66,
                [1, 1, 1, 2],
                id="should return [1, 1, 1, 2] when cents = 66"
            )
        ]
    )
    def test_coin_combination_calculation(
        self,
        cents: int,
        expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result
