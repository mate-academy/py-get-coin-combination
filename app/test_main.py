import pytest
from app.main import get_coin_combination


# write your tests here

class TestMainApp:
    @pytest.mark.parametrize(
        "number_of_coins,expected_amount",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (67, [2, 1, 1, 2]),
        ]
    )
    def test_correct(
            self,
            number_of_coins: int,
            expected_amount: list
    ) -> None:
        assert get_coin_combination(number_of_coins) == expected_amount
