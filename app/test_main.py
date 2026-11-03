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
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination_returns_expected_result(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


def test_returns_correct_combination_for_mixed_coins() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_combination_sum_equals_original_amount() -> None:
    result = get_coin_combination(99)

    total = (
        result[0]
        + result[1] * 5
        + result[2] * 10
        + result[3] * 25
    )

    assert total == 99
