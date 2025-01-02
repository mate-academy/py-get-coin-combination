from app.main import get_coin_combination
import pytest


class TestCoinCombinationClass:
    @pytest.mark.parametrize(
        "number, expected_value",
        [
            pytest.param(-1, [4, 0, 2, -1], id="test_coin_is_negative_number"),
            pytest.param(-1, [4, 0, 2, -1], id="test_coin_is_negative_number"),
        ]
    )
    def test_coin_is_negative_number(self,
                                     number: int,
                                     expected_value: list) -> None:
        assert get_coin_combination(number) == expected_value

    @pytest.mark.parametrize(
        "number, expected_error",
        [
            pytest.param("1", TypeError,
                         id="test_coin_is_integer"),
            pytest.param("2", TypeError,
                         id="test_coin_is_integer"),
        ]
    )
    def test_coin_is_integer(self,
                             number: int,
                             expected_error: Exception) -> None:
        with pytest.raises(expected_error):
            assert get_coin_combination(number) == expected_error

    @pytest.mark.parametrize(
        "number, expected_value",
        [
            pytest.param(6, [1, 1, 0, 0],
                         id="test_coin_is_positive_number"),
            pytest.param(50, [0, 0, 0, 2],
                         id="test_coin_is_positive_number"),
        ]
    )
    def test_coin_is_positive_number(self,
                                     number: int,
                                     expected_value: list) -> None:
        assert get_coin_combination(number) == expected_value

    @pytest.mark.parametrize(
        "number, expected_value",
        [
            pytest.param(50, [0, 0, 0, 2],
                         id="test_return_coins_of_the_different_types"),
            pytest.param(17, [2, 1, 1, 0],
                         id="test_return_coins_of_the_different_types"),
        ]
    )
    def test_return_coins_of_the_different_types(
            self,
            number: int,
            expected_value: list) -> None:
        assert get_coin_combination(number) == expected_value
