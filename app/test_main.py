import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should check zero cents"
            ),

            pytest.param(
                0.5,
                [0, 0, 0, 0],
                id="should check cents, which not an integer"
            ),

            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should check more than 1 cents"
            ),

            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should check more than 5 cents"
            ),

            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should check more than 10 cents"
            ),

            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should check more than 25 cents"
            ),

            pytest.param(
                117,
                [2, 1, 1, 4],
                id="should check large value working"
            ),
        ]
    )
    def test_converting_to_another_type_of_coins(
            self,
            cents: int,
            expected_result: list,
    ) -> None:
        assert get_coin_combination(cents) == expected_result

    @pytest.mark.parametrize(
        "cent",
        [
            pytest.param(
                "0",
                id="when data is string"
            ),
            pytest.param(
                [0],
                id="when data is list"
            ),
            pytest.param(
                {0},
                id="when data is set"
            ),

        ]
    )
    def test_type_of_result(
            self,
            cent: int,
    ) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cent)
