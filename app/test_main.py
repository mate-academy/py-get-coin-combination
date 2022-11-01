import pytest

from app.main import get_coin_combination


class TestCoinNominal:
    @pytest.mark.parametrize(
        "coin, nominal",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Only penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Penny and nickle"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="Penny, nickle and dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="Quarters"
            )
        ]
    )
    def test_nominal(self, coin: int, nominal: list) -> None:
        assert get_coin_combination(coin) == nominal
