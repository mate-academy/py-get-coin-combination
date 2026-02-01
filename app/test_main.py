import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (45, [0, 0, 2, 1]),
        (60, [0, 0, 1, 2]),
        (123, [3, 0, 2, 4])
    ],
    ids=[
        "test_returns_expected_coins_for_0",
        "test_returns_expected_coins_for_1",
        "test_returns_expected_coins_for_5",
        "test_returns_expected_coins_for_10",
        "test_returns_expected_coins_for_25",
        "test_returns_expected_coins_for_41",
        "test_returns_expected_coins_for_45",
        "test_returns_expected_coins_for_60",
        "test_returns_expected_coins_for_123",
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
