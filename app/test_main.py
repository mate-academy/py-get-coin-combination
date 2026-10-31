import pytest
from app.main import get_coin_combination


class TestGetCoinCombination():
    @pytest.mark.parametrize(
        "cents,expected",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="should return only zeros"
            ),
            pytest.param(
                1, [1, 0, 0, 0],
                id="should return only 1 penny"
            ),
            pytest.param(
                4, [4, 0, 0, 0],
                id="should return only only 4 nickels"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="should return only only 1 nickel"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="should return 1 penny and 1 nickel"
            ),
            pytest.param(
                9, [4, 1, 0, 0],
                id="should return 4 pennies and, 1 nickel"
            ),
            pytest.param(
                10, [0, 0, 1, 0],
                id="should return 1 penny and 1 dime"
            ),
            pytest.param(
                11, [1, 0, 1, 0],
                id="should return 1 penny and 1 dime"
            ),
            pytest.param(
                14, [4, 0, 1, 0],
                id="should return 4 pennies, and 1 dime"
            ),
            pytest.param(
                15, [0, 1, 1, 0],
                id="should return 1 nickels and 1 dime"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="should return 2 pennies, 1 nickel and 1 dime"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="should return only 1 quarters"
            ),
            pytest.param(
                30, [0, 1, 0, 1],
                id="should return 1 nickel and 1 quarters"
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="should return only 2 quarters"
            ),
            pytest.param(
                99, [4, 0, 2, 3],
                id="should return 4 penny, 2 dime and 3 quarters"
            ),
            pytest.param(
                100, [0, 0, 0, 4],
                id="should return only 4 quarters"
            ),
            pytest.param(
                250, [0, 0, 0, 10],
                id="should return only 10 quarters"
            ),
            pytest.param(
                888, [3, 0, 1, 35],
                id="should return 3 pennies, 1 dime, and 35 quarters"
            ),
            pytest.param(
                1111, [1, 0, 1, 44],
                id="should return 1 penny, 1 dime and 44 quarters"
            ),
            pytest.param(
                2000001, [1, 0, 0, 80000],
                id="should return 1 penny and 80000 quarters"
            ),
        ]
    )
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected
