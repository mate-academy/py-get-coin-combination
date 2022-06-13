from app.main import get_coin_combination


class TestGetCoinCombination:
    def test_zero_penny(self):
        assert get_coin_combination(0) == [0, 0, 0, 0]

    def test_one_penny(self):
        assert get_coin_combination(1) == [1, 0, 0, 0]

    def test_one_penny_and_one_nickel(self):
        assert get_coin_combination(6) == [1, 1, 0, 0]

    def test_one_penny_and_one_nickel_and_one_dime(self):
        assert get_coin_combination(16) == [1, 1, 1, 0]

    def test_one_penny_and_one_nickel_and_one_dime_and_one_quarter(self):
        assert get_coin_combination(41) == [1, 1, 1, 1]
