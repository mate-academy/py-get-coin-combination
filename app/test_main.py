import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cent_element, expected_list_of_cents",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],  # corrected this line
                id="""test should return first element
                of list 1 because 1penny = 1cent""",
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="""test should return first and second element
                of list 1 because 1penny = 1cent and 1nikel = 5 cent""",
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="""test should return first element 2 and
                second third elements 1 because 1penny = 1cent
                and 1nikel = 5 cent and 1dime = 10cent""",
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="""test should return fourth
                element 2 because 1quarter = 25cent""",
            ),
        ]
    )
    def test_get_coin_combination(self, cent_element: int,
                                  expected_list_of_cents: int) -> None:
        assert get_coin_combination(cent_element) == expected_list_of_cents
