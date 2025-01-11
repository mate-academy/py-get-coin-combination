import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "value",
        [
            0,
            50
        ]
    )
    def test_get_coin_combination_should_return_list_type(
        self,
        value: int
    ) -> None:
        assert type(get_coin_combination(value)) == list

    @pytest.mark.parametrize(
        "value",
        [
            0,
            50
        ]
    )
    def test_get_coin_combination_should_return_len_equals_4(
        self,
        value: int
    ) -> None:
        assert len(get_coin_combination(value)) == 4

    @pytest.mark.parametrize(
        "value, expected",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ]
    )
    def test_get_coin_combination_should_return_expected_results(
        self,
        value: int,
        expected: list
    ) -> None:
        assert get_coin_combination(value) == expected
