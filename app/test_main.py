import pytest
from app.main import get_coin_combination


class TestGetCoin:
    @pytest.mark.parametrize(
        "amount_cents,result",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="test should check when passing 0 coins"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="test should check when passing 1 coin"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="test should check when passing 5 coins"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="test should check when passing 6 coins"
            ),
            pytest.param(
                10, [0, 0, 1, 0],
                id="test should check when passing 10 coins"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="test should check when passing 17 coins"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="test should check when passing 25 coins"
            ),
            pytest.param(
                42, [2, 1, 1, 1],
                id="test should check when passing 42 coins"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            amount_cents: int,
            result: list[int]
    ) -> None:
        assert get_coin_combination(amount_cents) == result
