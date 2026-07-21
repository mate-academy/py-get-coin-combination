import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (6, [1, 1, 0, 0]),
            (11, [1, 0, 1, 0]),
            (16, [1, 1, 1, 0]),
            (25, [0, 0, 0, 1]),
            (47, [2, 0, 2, 1]),
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "string",
            None,
            [25],
            {"cents": 25},
        ]
    )
    def test_get_coin_combination_invalid_input(
            self,
            invalid_input: Exception
    ) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(invalid_input)
