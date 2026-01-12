import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (123456, [1, 1, 0, 4938])
    ]
)
def test_get_coin_combination(cents: object, expected: object) -> object:
    assert get_coin_combination(cents) == expected
