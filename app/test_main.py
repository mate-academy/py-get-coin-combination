from typing import Type

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected_result",
    [(1, [1, 0, 0, 0]),
     (6, [1, 1, 0, 0]),
     (17, [2, 1, 1, 0]),
     (50, [0, 0, 0, 2]),
     ]
)
def test_if_return_is_correct(
        cents: int,
        expected_result: list) -> None:
    assert expected_result == get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents,expected_error",
    [([], TypeError),
     ([-1], TypeError),
     ({14}, TypeError),
     ((14, 23), TypeError),
     ([15, 15], TypeError)]
)
def test_raise_errors_correctly(
        cents: int,
        expected_error: Type[BaseException]) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
