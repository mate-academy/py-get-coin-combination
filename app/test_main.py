from app.main import get_coin_combination
import pytest
from typing import Any


# write your tests here
class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,result",
        [
            (1005, [0, 1, 0, 40]),
            (101, [1, 0, 0, 4]),
            (48, [3, 0, 2, 1]),
            (15, [0, 1, 1, 0]),
            (2, [2, 0, 0, 0])
        ]
    )
    def test_correct_answer(self, cents: int, result: list[int]) -> None:
        assert get_coin_combination(cents) == result

    def test_negative_numbers(self) -> None:
        assert get_coin_combination(-2) == [3, 0, 2, -1]

    @pytest.mark.parametrize(
        "value,expected_error",
        [
            ("caption", TypeError)
        ]
    )
    def test_errors(self, value: Any, expected_error: type) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(value)
