import pytest

from app.main import get_coin_combination


class TestDiffNumbers:
    @pytest.mark.parametrize(
        "coins_to_count,number_of_coins",
        [
            pytest.param(
                1,
                [1, 0, 0, 0]
            ),
            pytest.param(
                6,
                [1, 1, 0, 0]
            ),
            pytest.param(
                17,
                [2, 1, 1, 0]
            ),
            pytest.param(
                50,
                [0, 0, 0, 2]
            )
        ]
    )
    def test_should_return_correct_number_of_coins(
            self,
            coins_to_count: int,
            number_of_coins: list
    ) -> None:
        assert get_coin_combination(coins_to_count) == number_of_coins
