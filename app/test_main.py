import pytest

from app.main import get_coin_combination


class TestMain:
    @pytest.mark.parametrize(
        "cents,result",
        [
            pytest.param(
                50, [0, 0, 0, 2], id="should convert 50 cents to 2 quarters"
            ),
            pytest.param(
                10, [0, 0, 1, 0], id="should convert 10 cents to 1 dime"
            ),
            pytest.param(
                5, [0, 1, 0, 0], id="should convert 5 cents to 1 nickel"
            ),
            pytest.param(
                3, [3, 0, 0, 0], id="should convert 3 cents to 3 nickel"
            ),
            pytest.param(
                17, [2, 1, 1, 0], id="should return correct result"
            )
        ]
    )
    def test_get_coin_combination(self, cents: int, result: list) -> None:
        assert get_coin_combination(cents) == result
