import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, coin_combination",
        [
            pytest.param(1, [1, 0, 0, 0],
                         id="for 1 cent possible combination is 1 penny"),
            pytest.param(6, [1, 1, 0, 0],
                         id="for 6 cents possible combination is 1 penny"
                            "and 1 nickel"),
            pytest.param(17, [2, 1, 1, 0],
                         id="for 17 cents possible combination is 2 pennies,"
                            "1 nickel and 1 dime"),
            pytest.param(50, [0, 0, 0, 2],
                         id="for 6 cents possible combination is 2 quarters"),
        ]
    )
    def test_return_correct_values(
            self,
            cents: int,
            coin_combination: list
    ) -> None:
        assert get_coin_combination(cents) == coin_combination

    @pytest.mark.parametrize(
        "cents",
        [
            ("1"),
            ([2]),
            ({2})
        ]
    )
    def test_receive_correct_value_type(
            self,
            cents: int
    ) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cents)
