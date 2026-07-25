from app.main import get_coin_combination


class TestCoin:
    def test_for_zero_penny(self):
        assert get_coin_combination(0) == [0, 0, 0, 0]

    def test_for_one_penny(self):
        assert get_coin_combination(1) == [1, 0, 0, 0]

    def test_return_nickels(self):
        assert get_coin_combination(7) == [2, 1, 0, 0]

    def test_return_dimes(self):
        assert get_coin_combination(17) == [2, 1, 1, 0]

    def test_return_quarters(self):
        assert get_coin_combination(39) == [4, 0, 1, 1]
