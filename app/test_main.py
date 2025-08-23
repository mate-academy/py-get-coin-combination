import pytest
import app.main as main


# --- Przykłady z treści zadania ---
@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_examples_from_spec(cents: int, expected: list[int]) -> None:
    assert main.get_coin_combination(cents) == expected


# --- Granica: 0 centów -> same zera ---
def test_zero_cents_returns_all_zeros() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


# --- Długość wyniku zawsze 4 (pennies, nickels, dimes, quarters) ---
@pytest.mark.parametrize("cents", [0, 1, 4, 5, 11, 24, 37, 99])
def test_length_is_always_four(cents: int) -> None:
    result = main.get_coin_combination(cents)
    assert len(result) == 4


# --- Wszystkie elementy muszą być intami i nieujemne ---
@pytest.mark.parametrize("cents", [0, 3, 17, 50, 99])
def test_all_elements_are_non_negative_integers(cents: int) -> None:
    result = main.get_coin_combination(cents)
    assert all(isinstance(x, int) for x in result)
    assert all(x >= 0 for x in result)


# --- Własność: suma monet * nominał = kwota wejściowa ---
@pytest.mark.parametrize("cents", [0, 1, 6, 17, 24, 37, 50, 74, 99])
def test_value_is_preserved(cents: int) -> None:
    pennies, nickels, dimes, quarters = main.get_coin_combination(cents)
    total = pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25
    assert total == cents


# --- Własność: kombinacja jest „chciwa” (minimalna) dla US coinów ---
@pytest.mark.parametrize(
    "cents",
    [0, 1, 4, 5, 9, 10, 17, 24, 28, 33, 41, 50, 67, 99],
)
def test_greedy_breakdown_matches_us_denominations(cents: int) -> None:
    pennies, nickels, dimes, quarters = main.get_coin_combination(cents)

    quarters_expected = cents // 25
    remainder_after_quarters = cents % 25

    dimes_expected = remainder_after_quarters // 10
    remainder_after_dimes = remainder_after_quarters % 10

    nickels_expected = remainder_after_dimes // 5
    pennies_expected = remainder_after_dimes % 5

    assert [pennies, nickels, dimes, quarters] == [
        pennies_expected,
        nickels_expected,
        dimes_expected,
        quarters_expected,
    ]
