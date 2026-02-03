import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_examples_from_description(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
    ],
)
def test_exact_coin_values_and_mixes(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [0, 1, 7, 19, 37, 99, 123])
def test_sum_matches_original_amount(cents: int) -> None:
    pennies, nickels, dimes, quarters = get_coin_combination(cents)
    total = pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25
    assert total == cents


@pytest.mark.parametrize("cents", [3, 8, 14, 37, 99])
def test_minimal_number_of_coins(cents: int) -> None:
    result = get_coin_combination(cents)
    greedy_count = sum(result)

    minimal_count = float("inf")
    for quarters in range(cents // 25 + 1):
        remaining_after_quarters = cents - 25 * quarters

        for dimes in range(remaining_after_quarters // 10 + 1):
            remaining_after_dimes = remaining_after_quarters - 10 * dimes

            for nickels in range(remaining_after_dimes // 5 + 1):
                pennies = remaining_after_dimes - 5 * nickels
                coin_count = quarters + dimes + nickels + pennies

                if coin_count < minimal_count:
                    minimal_count = coin_count

    assert greedy_count == minimal_count


def test_uses_different_coin_types_when_beneficial() -> None:
    result = get_coin_combination(17)
    used_types = sum(1 for count in result if count > 0)
    assert used_types >= 2
    assert result == [2, 1, 1, 0]
