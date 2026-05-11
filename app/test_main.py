import pytest
import app.main as main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (3, [3, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (50, [0, 0, 0, 2]),
        (75, [0, 0, 0, 3]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected
