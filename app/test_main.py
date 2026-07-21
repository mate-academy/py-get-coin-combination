from app.main import get_coin_combination
import unittest


class TestGetCoin(unittest.TestCase):
    def test_get_coin_with_zero(self) -> None:
        assert get_coin_combination(1) == [1, 0, 0, 0]

    def test_get_coin_with_two_different_coins(self) -> None:
        assert get_coin_combination(6) == [1, 1, 0, 0]

    def test_get_coin_with_three_different_coins(self) -> None:
        assert get_coin_combination(17) == [2, 1, 1, 0]

    def test_get_coin_with_four_different_coins(self) -> None:
        assert get_coin_combination(41) == [1, 1, 1, 1]
