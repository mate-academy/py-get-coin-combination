import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    def test_get_coin_combination_should_return_type_list(self) -> None:
        assert (
            isinstance(get_coin_combination(65), list)
        ), "Function result should be equal type list"

    @pytest.mark.parametrize(
        "cents, result_list",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return list "
                   "with coin combination where shows 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return list "
                   "with coin combination where shows 1 penny + 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return list with coin combination "
                   "where shows 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return list "
                   "with coin combination where shows 2 quarters"
            )
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            result_list: list
    ) -> None:
        assert get_coin_combination(cents) == result_list
