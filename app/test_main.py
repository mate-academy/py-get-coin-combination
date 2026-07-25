import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="zero cents"
            ),
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="less then 5 coins"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="equal 5 coins"
            ),
            pytest.param(
                7,
                [2, 1, 0, 0],
                id="between 5 and 10 coins"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="equal 10 coins"
            ),
            pytest.param(
                13,
                [3, 0, 1, 0],
                id="between 10 and 15 coins"
            ),
            pytest.param(
                19,
                [4, 1, 1, 0],
                id="between 15 and 20 coins"
            ),
            pytest.param(
                20,
                [0, 0, 2, 0],
                id="equal 20 coins"
            ),
            pytest.param(
                24,
                [4, 0, 2, 0],
                id="between 20 and 25 coins"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="equal 25 coins"
            ),
            pytest.param(
                125,
                [0, 0, 0, 5],
                id="more then 25 coins if divider 25"
            ),
            pytest.param(
                143,
                [3, 1, 1, 5],
                id="more then 25 coins if not divider 25"
            ),
        ]
    )
    def test_get_coin_combination(
            self,
            cents,
            expected_result
    ):
        assert get_coin_combination(cents) == expected_result
