import pytest

from app.main import get_coin_combination


class TestCoin:
    @pytest.mark.parametrize("cents, expected", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ])
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            ("10",
             None,
             [10],
             {"cents": 5},
             )
        ]
    )
    def test_get_coin_combination_invalid_type(self, invalid_input) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(invalid_input)
