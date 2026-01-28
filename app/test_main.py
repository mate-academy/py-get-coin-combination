import pytest

from app.main import get_coin_combination


class TestCents:
    @pytest.mark.parametrize("cents, expected", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1])
    ])
    def test_get_coin_combination(self,
                                  cents: int,
                                  expected: list[int]) -> None:
        assert get_coin_combination(cents) == expected
