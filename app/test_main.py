from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("input_value, expected", [
    (1, [1, 0, 0, 0]),
    (9, [4, 1, 0, 0]),
    (12, [2, 0, 1, 0])
])
def test_get_coin_combination_function(input_value: int,
                                       expected: list[int]) -> None:
    assert get_coin_combination(input_value) == expected
