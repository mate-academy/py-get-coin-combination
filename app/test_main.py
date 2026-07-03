import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "number_of_cents,expected_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should return all zeros when given 0"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return one penny when given 1"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="should return one nickel when given 5"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="should return one dime when given 10"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="should return one quarter when given 25"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="should return all 1 when given 41"
            ),
            pytest.param(
                892374,
                [4, 0, 2, 35694],
                id="checking huge number of cents"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            number_of_cents: int,
            expected_list: list[int]
    ) -> None:
        assert get_coin_combination(number_of_cents) == expected_list

    @pytest.mark.parametrize(
        "number_of_cents,expected_error",
        [
            pytest.param(
                [5],
                TypeError,
                id="should raise error if list type given"
            ),
            pytest.param(
                "ten",
                TypeError,
                id="should raise error if string type given"
            ),
            pytest.param(
                {1: 2},
                TypeError,
                id="should raise error if dict type given"
            )
        ]
    )
    def test_get_coin_combination_error(
            self,
            number_of_cents: list[int] | str | dict,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(number_of_cents)
