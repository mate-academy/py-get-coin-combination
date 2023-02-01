import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "initial_cents,expected_coins_list",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (95, [0, 0, 2, 3]),
        (119, [4, 1, 1, 4]),
        (322, [2, 0, 2, 12]),
        (0, [0, 0, 0, 0])
    ],
)
def test_should_return_equal_list(
    initial_cents: int,
    expected_coins_list: list
) -> None:
    assert get_coin_combination(initial_cents) == expected_coins_list
