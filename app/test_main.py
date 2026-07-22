from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "actual, expected",
    [
        (get_coin_combination(1), [1, 0, 0, 0]),
        (get_coin_combination(6), [1, 1, 0, 0]),
        (get_coin_combination(17), [2, 1, 1, 0]),
        (get_coin_combination(50), [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(actual: list, expected: list) -> None:
    assert actual == expected
