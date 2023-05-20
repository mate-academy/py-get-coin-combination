import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,combination_list",
        [
            pytest.param(
                6,
                [1, 1, 0, 0],
                id=("when the number of coins is 6,"
                    "the output should be - [1, 1, 0, 0]")
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id=("when the number of coins is 0,"
                    "the output should be - [0, 0, 0, 0]")
            ),
            pytest.param(
                4,
                [4, 0, 0, 0],
                id=("when the number of coins is 4,"
                    "the output should be - [4, 0, 0, 0]")
            ),
            pytest.param(
                1000,
                [0, 0, 0, 40],
                id=("when the number of coins is 1000,"
                    "the output should be - [0, 0, 0, 40]")
            ),
            pytest.param(
                1001,
                [1, 0, 0, 40],
                id=("when the number of coins is 1001,"
                    "the output should be - [1, 0, 0, 40]")
            ),
            pytest.param(
                1006,
                [1, 1, 0, 40],
                id=("when the number of coins is 1006,"
                    "the output should be - [1, 1, 0, 40]")
            ),
            pytest.param(
                1016,
                [1, 1, 1, 40],
                id=("when the number of coins is 1016,"
                    "the output should be - [1, 1, 1, 40]")
            ),
            pytest.param(
                -10,
                [0, 1, 1, -1],
                id=("when the number of coins is negative (-10),"
                    "the output should be - [0, 1, 1, -1]")
            ),
            pytest.param(
                10.9,
                [0, 0, 1, 0],
                id=("when the number of coins is float (10.9),"
                    "the output should be floored - [0, 0, 1, 0]")
            ),

        ]
    )
    def test_coin_combination(
            self,
            cents: int,
            combination_list: list
    ) -> None:
        assert get_coin_combination(cents) == combination_list

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            pytest.param(
                "hello",
                TypeError
            ),
            pytest.param(
                {},
                TypeError
            ),
        ]
    )
    def test_expected_error(
            self,
            cents: any,
            expected_error: TypeError
    ) -> None:
        print(cents)
        with pytest.raises(expected_error):
            get_coin_combination(cents)
