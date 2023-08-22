import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="test for each coin in result"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="test only quarter coin"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="test 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test zero coins if cents is zero"
            ),
            pytest.param(
                11,
                [1, 0, 1, 0],
                id="test 1 penny + 1 dime"
            ),
        ]
    )
    def test_should_return_correct_values(
            self,
            cents: int,
            expected_result: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_result
