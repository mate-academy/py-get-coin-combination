import pytest
import app.main as main


DATA = [
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (50, [0, 0, 0, 2]),
    (0, [0, 0, 0, 0]),
    (99, [4, 0, 2, 3]),
]


@pytest.mark.parametrize("value, expected", DATA)
def test_get_coin_combination(value: int, expected: list) -> None:
    assert main.get_coin_combination(value) == expected
