import pytest
from app.main import get_coin_combination


class TestGetCoinCombinationClass:

    @pytest.mark.parametrize(
        "cents, result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_valus_get_coins_combination(self, cents: int, result: list) -> None:
        assert get_coin_combination(cents) == result
