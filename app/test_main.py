import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins_list",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (40, [0, 1, 1, 1]),
        (50, [0, 0, 0, 2])
    ]
)
def test_check_correct_coin_combination(
        cents: int,
        coins_list: list
) -> None:
    assert get_coin_combination(cents) == coins_list
