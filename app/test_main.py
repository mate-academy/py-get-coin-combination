from app.main import get_coin_combination

import pytest


class TestGetCoinCombination:
    def test_should_return_type_of_result_is_list(self) -> None:
        assert isinstance(get_coin_combination(0), list)

    def test_should_return_len_of_list_is_4(self) -> None:
        assert len(get_coin_combination(0)) == 4

    @pytest.mark.parametrize(
        "count_of_cents,expected_result",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="convert to pennies from 0 to 5 cents"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="convert 5 cents to nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="convert 10 cents to dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="convert 25 cents to quarter"
            )
        ]
    )
    def test_calculate_coins_correctly(
            self,
            count_of_cents: int,
            expected_result: list[int]
    ) -> None:
        assert get_coin_combination(count_of_cents) == expected_result
