import pytest

from app.main import get_coin_combination


class Tests:
    @pytest.mark.parametrize(
        "cents, result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="If value = zero, func should be return not empty list"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Function should be return 1 pennie"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="Function should be return 1 pennie and 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="Function should be return 2 pennies, 1 nickel and 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="Function should be return 2 quarters"
            )
        ]
    )
    def test_func(self, cents: int, result: list) -> None:
        assert get_coin_combination(cents) == result
