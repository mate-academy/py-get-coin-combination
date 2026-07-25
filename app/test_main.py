import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_combination",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="must return 0 for if no cents"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id=("must add zero when the nominal "
                    "of coin < of the value in the list")
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="must add zero to smaller nominal of coins"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="must return correct result with every nominal of coins"
            )
        ]
    )
    def test_coin_combination(self,
                              cents: int,
                              expected_combination: list) -> None:
        assert get_coin_combination(cents) == expected_combination
