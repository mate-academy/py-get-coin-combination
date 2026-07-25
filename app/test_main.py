from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("coin_combination, expected", [
    (get_coin_combination(0), [0, 0, 0, 0]),
    (get_coin_combination(1), [1, 0, 0, 0]),
    (get_coin_combination(5), [0, 1, 0, 0]),
    (get_coin_combination(10), [0, 0, 1, 0]),
    (get_coin_combination(25), [0, 0, 0, 1]),
    (get_coin_combination(30), [0, 1, 0, 1]),
    (get_coin_combination(99), [4, 0, 2, 3]),
])
def test_get_coin_combination(coin_combination: list, expected: list) -> None:
    assert coin_combination == expected


def test_get_coin_combination_negative() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)
