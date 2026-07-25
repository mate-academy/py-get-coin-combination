from app.main import get_coin_combination


class TestGetCoinCombination:
    def test_if_0_coins(self):
        goals = get_coin_combination(0)
        assert goals == [0, 0, 0, 0]

    def test_if_coins_only_penny(self):
        goals = get_coin_combination(2)
        assert goals == [2, 0, 0, 0]

    def test_coins_with_nickel(self):
        goals = get_coin_combination(7)
        assert goals == [2, 1, 0, 0]

    def test_coins_with_dimes(self):
        goals = get_coin_combination(17)
        assert goals == [2, 1, 1, 0]

    def test_coins_with_quarters(self):
        goals = get_coin_combination(56)
        assert goals == [1, 1, 0, 2]

    def test_all_coins(self):
        goals = get_coin_combination(41)
        assert goals == [1, 1, 1, 1]
