import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(50, [0, 0, 0, 2]),
            pytest.param(17, [2, 1, 1, 0]),
            pytest.param(6, [1, 1, 0, 0]),
            pytest.param(1, [1, 0, 0, 0])
        ])
    def test_can_return_proper_combination(self,
                                           cents: int,
                                           expected: list[int]) -> None:
        assert get_coin_combination(cents) == expected

# write your tests here
