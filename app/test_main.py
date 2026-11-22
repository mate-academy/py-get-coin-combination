import pytest

import app.main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (10, [0, 0, 1, 0]),
        (9, [4, 1, 0, 0]),
        (5, [0, 1, 0, 0])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert app.main.get_coin_combination(cents) == expected
