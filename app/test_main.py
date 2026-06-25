import pytest
from app.main import get_coin_combination


class TestBasicCases:
    @pytest.mark.parametrize("cent, expected", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
    ])
    def test_basic(self, cent: int, expected: list) -> None:
        assert get_coin_combination(cent) == expected


class TestEdgesCases:
    @pytest.mark.parametrize("cent, expected", [
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),

    ])
    def test_basic(self, cent: int, expected: list) -> None:
        assert get_coin_combination(cent) == expected
