import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coin, expected",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (1500, [0, 0, 0, 60]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_get_coin_combination(
            self,
            coin: int,
            expected: list) -> None:
        assert get_coin_combination(coin) == expected
