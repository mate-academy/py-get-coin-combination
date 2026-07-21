import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            pytest.param(1, [1, 0, 0, 0], id="Test for one cents"),
            pytest.param(6, [1, 1, 0, 0], id="Test for 1 nickel and 1 cent"),
            pytest.param(
                17, [2, 1, 1, 0], id="Test for 2 pennies, nickel and dime"
            ),
            pytest.param(50, [0, 0, 0, 2], id="Test 2 quarters"),
        ],
    )
    def test_check_correct_convert(
        self, cents: int, expected_result: list
    ) -> None:
        result = get_coin_combination(cents)
        assert result == expected_result
