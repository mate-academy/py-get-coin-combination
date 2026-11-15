import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_combination",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test zero cent"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="test one cent"
            ),
            pytest.param(
                2,
                [2, 0, 0, 0],
                id="test two cents"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="test five cents"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="test six cents"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="test ten cents"
            ),
            pytest.param(
                15,
                [0, 1, 1, 0],
                id="test fifteen cents"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="test seventeen cents"
            ),
            pytest.param(
                24,
                [4, 0, 2, 0],
                id="test twenty four cents"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="test twenty five cents"
            ),
            pytest.param(
                26,
                [1, 0, 0, 1],
                id="test twenty six cents"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="test forty one cents"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="test fifty cents"
            ),
        ]
    )
    def test_coin_combination_correctly(
        self,
        cents: int,
        expected_combination: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_combination
