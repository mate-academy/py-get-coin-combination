import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents, expected_combination",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ],
        ids=[
            "1 coins should be return combination [1, 0, 0, 0]",
            "6 coins should be return combination [1, 1, 0, 0]",
            "17 coins should be return combination [2, 1, 1, 0]",
            "50 coins should be return combination [0, 0, 0, 2]",
        ]
    )
    def test_should_return_coin_combination(
            self,
            cents: int,
            expected_combination: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_combination
