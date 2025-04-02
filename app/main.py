import unittest


def get_coin_combination(cents: int) -> list[int]:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins


class TestGetCoinCombination(unittest.TestCase):
    def test_zero_cents(self) -> None:
        self.assertEqual(get_coin_combination(0), [0, 0, 0, 0])

    def test_only_pennies(self) -> None:
        self.assertEqual(get_coin_combination(4), [4, 0, 0, 0])

    def test_only_nickels(self) -> None:
        self.assertEqual(get_coin_combination(5), [0, 1, 0, 0])

    def test_only_dimes(self) -> None:
        self.assertEqual(get_coin_combination(10), [0, 0, 1, 0])

    def test_only_quarters(self) -> None:
        self.assertEqual(get_coin_combination(25), [0, 0, 0, 1])

    def test_mixed_coins(self) -> None:
        self.assertEqual(get_coin_combination(41), [1, 1, 1, 1])
        self.assertEqual(get_coin_combination(99), [4, 0, 2, 3])

    def test_large_number(self) -> None:
        self.assertEqual(get_coin_combination(100), [0, 0, 0, 4])
        self.assertEqual(get_coin_combination(123), [3, 0, 2, 4])


if __name__ == "__main__":
    unittest.main()
