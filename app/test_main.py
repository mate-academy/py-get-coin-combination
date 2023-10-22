import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_combination",
    [
        (10, [0, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (0, [0, 0, 0, 0]),
        (1000, [0, 0, 0, 40]),
        (56, [1, 1, 1, 2]),
        (24, [4, 0, 2, 0])
    ]
)
def test_get_coin_combination(cents: int, expected_combination: int) -> None:
    assert get_coin_combination(cents) == expected_combination
