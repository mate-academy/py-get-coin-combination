import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            pytest.param(0, [0, 0, 0, 0], id="should return 0 coins"),
            pytest.param(1, [1, 0, 0, 0], id="should return 1 penny"),
            pytest.param(5, [0, 1, 0, 0], id="should return 1 nickel"),
            pytest.param(10, [0, 0, 1, 0], id="should return 1 dime"),
            pytest.param(25, [0, 0, 0, 1], id="should return 1 quarter"),
            pytest.param(41, [1, 1, 1, 1], id="should return every 1 coin"),
        ],
    )
    def test_get_correct_coins_amount(
        self, cents: int, expected_result: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_result
