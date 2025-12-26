from typing import Any

from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 cent should be 1, 0, 0, 0 coins",
        "6 cents should be 1, 1, 0, 0 coins",
        "17 cents should be 2, 1, 1, 0 coins",
        "50 cents should be 0, 0, 0, 2 coins",
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        pytest.param("a", TypeError, id="cents should be integer")
    ]
)
def test_get_coin_combination_for_errors(
        cents: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        assert get_coin_combination(cents)
