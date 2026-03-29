import pytest

from app.main import get_coin_combination


class NonNegativeError(Exception):
    pass


class NotFloatError(Exception):
    pass


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_list",
        [
            (1, [1, 0, 0, 0]),
            (3, [3, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (50, [0, 0, 0, 2]),
            (17, [2, 1, 1, 0]),
            (10000, [0, 0, 0, 400])
        ]
    )
    def test_if_argument_is_instance_int(self, cents, expected_list):
        assert get_coin_combination(cents) == expected_list

    def test_if_argument_equal_zero(self):
        assert get_coin_combination(0) == [0, 0, 0, 0]

    def test_if_argument_equal_negative_int(self):
        try:
            get_coin_combination(-1)
            raise NonNegativeError
        except NonNegativeError:
            print("Cents must be non-negative integer")

    def test_if_argument_is_instance_float(self):
        try:
            get_coin_combination(1.5)
            raise NotFloatError
        except NotFloatError:
            print("Cents must be integer")
