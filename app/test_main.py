from typing import Any

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="1 penny 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
        pytest.param(10, [0, 0, 1, 0], id="1 dime"),
        pytest.param(5, [0, 1, 0, 0], id="1 nickel"),
    ]
)
def test_works_correctly(cents: int, expected_result: list[int]) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        pytest.param(-5, ValueError, id="Value error test"),
        pytest.param("5", TypeError, id="TypeError test"),
    ]
)
def test_raises_errors_correctly(cents: int, expected_error: Any) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
