import pytest

from app.main import get_coin_combination


class TestMain:
    @pytest.mark.parametrize(
        "cents,coins",
        [
            pytest.param(0, [0, 0, 0, 0], id="if 0 cents"),
            pytest.param(1, [1, 0, 0, 0], id="if 1 cent"),
            pytest.param(4, [4, 0, 0, 0], id="if 4 cents"),
            pytest.param(5, [0, 1, 0, 0], id="if 5 cents"),
            pytest.param(9, [4, 1, 0, 0], id="if 9 cents"),
            pytest.param(10, [0, 0, 1, 0], id="if 10 cents"),
            pytest.param(24, [4, 0, 2, 0], id="if 24 cents"),
            pytest.param(25, [0, 0, 0, 1], id="if 25 cents"),
            pytest.param(41, [1, 1, 1, 1], id="if all coins"),
            pytest.param(337, [2, 0, 1, 13], id="if many coins")
        ]
    )
    def test_get_coin_combination(self, cents: int, coins: list) -> None:
        assert get_coin_combination(cents) == coins

    # def test_error(self):
    #     with pytest.raises(AssertionError):
    #         get_coin_combination(-2)
