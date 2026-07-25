import unittest

from app.main import get_coin_combination


class TestGetCoinCombination(unittest.TestCase):
    def test_exact_quarters(self) -> None:
        self.assertEqual(get_coin_combination(25), [0, 0, 0, 1])
        self.assertEqual(get_coin_combination(50), [0, 0, 0, 2])

    def test_combination_of_coins(self) -> None:
        self.assertEqual(get_coin_combination(41), [1, 1, 1, 1])
        self.assertEqual(get_coin_combination(99), [4, 0, 2, 3])

    def test_single_coin_types(self) -> None:
        self.assertEqual(get_coin_combination(5), [0, 1, 0, 0])
        self.assertEqual(get_coin_combination(10), [0, 0, 1, 0])
        self.assertEqual(get_coin_combination(25), [0, 0, 0, 1])

    def test_edge_cases(self) -> None:
        self.assertEqual(get_coin_combination(1), [1, 0, 0, 0])
        self.assertEqual(get_coin_combination(123), [3, 0, 2, 4])

    def test_large_mixed_amount(self) -> None:
        self.assertEqual(get_coin_combination(58), [3, 1, 0, 2])

    def test_multiple_combinations(self) -> None:
        self.assertEqual(get_coin_combination(87), [2, 0, 1, 3])
        self.assertEqual(get_coin_combination(37), [2, 0, 1, 1])
