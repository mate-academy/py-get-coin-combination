import pytest


from app.main import get_coin_combination


class TestCoins:
    @pytest.mark.parametrize(
        "coin, result",
        [
            pytest.param(1, [1, 0, 0, 0]),
            pytest.param(5, [0, 1, 0, 0]),
            pytest.param(10, [0, 0, 1, 0]),
            pytest.param(25, [0, 0, 0, 1]),
            pytest.param(6, [1, 1, 0, 0]),
            pytest.param(15, [0, 1, 1, 0]),
            pytest.param(35, [0, 0, 1, 1]),
            pytest.param(16, [1, 1, 1, 0]),
            pytest.param(40, [0, 1, 1, 1]),
            pytest.param(0, [0, 0, 0, 0]),
            pytest.param(100, [0, 0, 0, 4]),
            pytest.param(17, [2, 1, 1, 0]),
            pytest.param(41, [1, 1, 1, 1])
        ]
    )
    def test_should_work(
            self,
            coin: int,
            result: list
    ) -> None:
        wyn = get_coin_combination(coin)
        assert wyn == result
