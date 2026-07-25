from app.main import get_coin_combination
import pytest


class TestDifSimpCases:
    @pytest.mark.parametrize(
        "cents,result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (0, [0, 0, 0, 0])
        ]
    )
    def test_different_simple_cases(self, cents: int, result: list) -> None:
        assert get_coin_combination(cents) == result
