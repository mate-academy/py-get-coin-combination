import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "initial_cents, list_coins",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="'coins' should equal to [0, 0, 0, 0] when 'cents' = 0"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="'coins' should equal to [1, 0, 0, 0] when 'cents' = 1"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="'coins' should equal to [1, 1, 0, 0] when 'cents' = 6"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="'coins' should equal to [2, 1, 1, 0] when 'cents' = 17"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="'coins' should equal to [0, 0, 0, 2] when 'cents' = 50"
            ),
        ]
    )
    def test_get_coin_combination_correctly(
            self,
            initial_cents: int,
            list_coins: list
    ) -> None:
        assert get_coin_combination(initial_cents) == list_coins
