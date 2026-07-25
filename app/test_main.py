import pytest

from app.main import get_coin_combination


class TestError:
    def test_type_error(self):
        with pytest.raises(TypeError):
            get_coin_combination([2])


class TestGetCoinCombination:
    def test_zero_cents_should_equal_zero(self):
        assert get_coin_combination(0) == [0, 0, 0, 0]

    def test_from_one_to_four_cent(self):
        assert get_coin_combination(4) == [4, 0, 0, 0]

    def test_from_five_to_nine_cent(self):
        assert get_coin_combination(7) == [2, 1, 0, 0]

    def test_from_ten_to_twenty_four_cent(self):
        assert get_coin_combination(19) == [4, 1, 1, 0]

    def test_from_twenty_five_and_more_cent(self):
        assert get_coin_combination(42) == [2, 1, 1, 1]
