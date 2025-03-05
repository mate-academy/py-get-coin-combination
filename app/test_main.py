import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_coins",
        [
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (100, [0, 0, 0, 4]),
            (1000, [0, 0, 0, 40]),
            (9999, [4, 0, 2, 399])
        ],
        ids=[
            "checkin with 5 coin",
            "checkin with 10 coin",
            "checkin with 25 coin",
            "checkin with 100 coin",
            "checkin with 1000 coin",
            "checkin with 9999 coin (big value)"
        ]
    )
    def test_coin_correct_value(self, cents: int, expected_coins: list) -> None:
        assert get_coin_combination(cents) == expected_coins
