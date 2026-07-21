from app.main import get_coin_combination


class TestGetCoinCombination:
    def test_value_cents_equals_0(self) -> None:
        cents = 0
        result = get_coin_combination(cents)
        assert result == [0, 0, 0, 0]

    def test_value_cents_equals_41(self) -> None:
        cents = 41
        result = get_coin_combination(cents)
        assert result == [1, 1, 1, 1]
