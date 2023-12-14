import pytest

from app.main import get_coin_combination


class TestMain:
    @pytest.mark.parametrize(
        "coin, list_of_cents",
        [
            pytest.param(1, [1, 0, 0, 0]),
            pytest.param(6, [1, 1, 0, 0]),
            pytest.param(17, [2, 1, 1, 0]),
            pytest.param(50, [0, 0, 0, 2])
        ]
    )
    def test_get_coin_combination(
            self,
            coin: int,
            list_of_cents: list) -> None:
        assert get_coin_combination(coin) == list_of_cents
