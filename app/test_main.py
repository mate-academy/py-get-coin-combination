from app.main import get_coin_combination


class TestGetCoinCombination:

    def test_for_one_penny(self):
        assert get_coin_combination(1) == [1, 0, 0, 0]

    def test_for_one_penny_plus_one_nickel(self):
        assert get_coin_combination(6) == [1, 1, 0, 0]

    def test_for_two_pennies_plus_one_nickel_plus_one_dime(self):
        assert get_coin_combination(17) == [2, 1, 1, 0]

    def test_for_two_quarters(self):
        assert get_coin_combination(50) == [0, 0, 0, 2]
