import pytest

from app.main import get_coin_combination


class TestCoin:
    @pytest.mark.parametrize("cents, coins", [
        pytest.param(1, [1, 0, 0, 0], id="1 cent test"),
        pytest.param(5, [0, 1, 0, 0], id="5 cents test"),
        pytest.param(10, [0, 0, 1, 0], id="10 cents test"),
        pytest.param(25, [0, 0, 0, 1], id="25 cents test"),
        pytest.param(66, [1, 1, 1, 2], id="66 cents test")
    ])
    def test_coin_combinations(self, cents: int, coins: list) -> None:
        assert get_coin_combination(cents) == coins
