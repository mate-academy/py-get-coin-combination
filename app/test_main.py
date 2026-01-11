from app.main import get_coin_combination

import pytest

from typing import Any


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (0, [0, 0, 0, 0]),
    (73, [3, 0, 2, 2]),
])
def test_get_coin_combination(cents: Any, expected: list) -> None:
    assert get_coin_combination(cents) == expected
