import pytest

from app.main import get_coin_combination


class TestCoins:
    @pytest.mark.parametrize(
        "cents,combination",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="should check 0 coins"),
            pytest.param(
                1, [1, 0, 0, 0],
                id="should check less then 5 coins"),
            pytest.param(
                5, [0, 1, 0, 0],
                id="should check 5 coins"),
            pytest.param(
                6, [1, 1, 0, 0],
                id="should check between 6-9 coins"),
            pytest.param(
                10, [0, 0, 1, 0],
                id="should check 10 coins"),
            pytest.param(
                17, [2, 1, 1, 0],
                id="should check between 10-24 coins"),
            pytest.param(
                25, [0, 0, 0, 1],
                id="should check 25 coins"),
            pytest.param(
                50, [0, 0, 0, 2],
                id="should check more than 25 coins")
        ]
    )
    def test_combinations(
            self,
            cents: int,
            combination: list
    ) -> None:
        assert get_coin_combination(cents) == combination
