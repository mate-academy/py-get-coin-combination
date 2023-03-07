from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected", [
            pytest.param(0, [0, 0, 0, 0],
                         id="no money - no coins"),
            pytest.param(7, [2, 1, 0, 0],
                         id="should return different coins"),
            pytest.param(11, [1, 0, 1, 0],
                         id="should return 1 dim and 1 penny"),
            pytest.param(42, [2, 1, 1, 1],
                         id="should return all kinds of coins")
        ]
    )
    def test_count_human_age_correctly(self,
                                       cents: int,
                                       expected: list
                                       ) -> None:
        assert get_coin_combination(cents) == expected
