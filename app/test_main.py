from app.main import get_coin_combination


class TestCoin:
    def test_if_coin_is_zero(self):
        assert get_coin_combination(0) == [0, 0, 0]

    def test_if_coin_is_one(self):
        assert get_coin_combination(1) == [1, 0, 0, 0]

    def test_return_nickels(self):
        assert get_coin_combination(6) == [1, 1, 0, 0]

    def test_return_dimes(self):
        assert get_coin_combination(17) == [2, 1, 1, 0]

    def test_return_quarters(self):
        assert get_coin_combination(50) == [0, 0, 0, 2]
