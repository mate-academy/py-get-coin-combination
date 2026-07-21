from app.main import get_coin_combination


class TestGetCoinCombination:
    def test_takes_zero_cent(self) -> None:
        assert get_coin_combination(0) == [0, 0, 0, 0]

    def test_should_return_one_penny(self) -> None:
        assert get_coin_combination(1) == [1, 0, 0, 0]

    def test_should_return_penny_and_nickel(self) -> None:
        assert get_coin_combination(6) == [1, 1, 0, 0]

    def test_should_return_coins_of_all_denominations(self) -> None:
        assert get_coin_combination(41) == [1, 1, 1, 1]

    def test_should_return_2_quarters(self) -> None:
        assert get_coin_combination(50) == [0, 0, 0, 2]
