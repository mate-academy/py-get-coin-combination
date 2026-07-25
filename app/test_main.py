from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination_parametrize(value: int,
                                          expected: list[int]) -> None:
    assert get_coin_combination(value) == expected
