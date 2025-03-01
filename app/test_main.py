import pytest

from app.main import get_coin_combination


test_data = [0, 1, 2, 3, 4, 5, 10, 25]


@pytest.mark.parametrize("cents", test_data)
class TestCoinCombination:
    def test_pennies_should_be_less_then_5(self, cents: int) -> None:
        result = get_coin_combination(cents)
        assert result[0] < 5

    def test_nickels_should_be_less_then_2(self, cents: int) -> None:
        result = get_coin_combination(cents)
        assert result[1] < 2

    def test_dimes_should_be_less_then_3(self, cents: int) -> None:
        result = get_coin_combination(cents)
        assert result[2] < 3


def test_could_return_coins_of_the_different_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
