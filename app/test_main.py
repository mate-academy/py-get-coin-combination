import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_coin_combination",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ]
    )
    def test_get_coin_combination_correctly(
            self,
            cents: int,
            expected_coin_combination: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_coin_combination, (
            f"Your result for {cents} cents "
            f"should be {expected_coin_combination}"
        )
