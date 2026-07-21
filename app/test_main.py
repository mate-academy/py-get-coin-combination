from typing import Any
from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (1256, [1, 1, 0, 50])
    ]
)
def test_get_coin_combination_with_different_results(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("abc", TypeError),
        ([], TypeError)
    ]
)
def test_get_coin_combination_unsuitable_value(
        value: Any,
        expected_error: BaseException
) -> None:
    with pytest.raises(TypeError):
        assert get_coin_combination(value)
