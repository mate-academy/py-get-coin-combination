from app.main import get_coin_combination
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(-1, [4, 0, 2, -1]),
        pytest.param(0, [0, 0, 0, 0]),
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(50, [0, 0, 0, 2]),
        pytest.param(40985, [0, 0, 1, 1639])
    ]
)
def test_get_coin_combination(cents: int,
                              expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param("cent", TypeError),
        pytest.param([1, 2, 3], TypeError),
        pytest.param(None, TypeError),
    ]
)
def test_should_raise_errors(cents: Any,
                             expected: Exception) -> None:
    with pytest.raises(expected):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cent,expected",
    [
        (True, [1, 0, 0, 0]),
        (False, [0, 0, 0, 0]),
    ]
)
def test_cent_equal_bool(cent: bool,
                         expected: list[int]) -> None:
    assert get_coin_combination(cent) == expected
