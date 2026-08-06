import pytest
import app.main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert app.main.get_coin_combination(cents) == expected
