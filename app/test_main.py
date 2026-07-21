from app.main import get_coin_combination


class TestGetCoinCombination:

    def test_one_pennie(self) -> None:
        assert get_coin_combination(1) == [1, 0, 0, 0]

    def test_pennie_and_nickel(self) -> None:
        assert get_coin_combination(6) == [1, 1, 0, 0]

    def test_pennie_nickel_dime(self) -> None:
        assert get_coin_combination(17) == [2, 1, 1, 0]

    def test_quarters(self) -> None:
        assert get_coin_combination(50) == [0, 0, 0, 2]
