import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="0 coin combination equals 0"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="1 coin combination equals one penni"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="1 coin combination equals one nickel"
            ),
            pytest.param(
                10, [0, 0, 1, 0],
                id="1 coin combination equals one dime"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="1 coin combination equals one quarter"
            ),
            pytest.param(
                67, [2, 1, 1, 2],
                id="combination equals 2 pennies 1 nickel 1 dime 1 quarter")
        ]
    )
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected

    def test_invalid_input(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("abc")
