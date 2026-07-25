from typing import Any

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(
        cents: int,
        expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param("1", TypeError),
        pytest.param(2.5, TypeError),
    ]
)
def test_get_coin_combination_with_type_error(
        cents: Any,
        expected: type[TypeError],
) -> None:
    with pytest.raises(expected):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(-2, ValueError),
        pytest.param(-5, ValueError),
    ]
)
def test_get_coin_combination_with_negative_value_error(
        cents: int,
        expected: type[ValueError],
) -> None:
    with pytest.raises(expected):
        get_coin_combination(cents)
