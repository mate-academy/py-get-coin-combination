import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coint,expected",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="shoud return zeroes list when cent equal 0"
            ),
            pytest.param(
                3, [3, 0, 0, 0],
                id="shoud return result when cent equal 3"
            ),
            pytest.param(
                8, [3, 1, 0, 0],
                id="shoud return result when cent equal 8"
            ),
            pytest.param(
                19, [4, 1, 1, 0],
                id="shoud return result when cent equal 19"
            ),
            pytest.param(
                78, [3, 0, 0, 3],
                id="shoud return result when cent equal 78"
            )
        ]
    )
    def test_modify_exchange_coins(self, coint: int,
                                   expected: list) -> None:
        assert get_coin_combination(coint) == expected
