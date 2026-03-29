# import pytest
from app.main import get_coin_combination


def test_the_sum_of_all_coins_should_be_equal_cents_value() -> None:
    coins = get_coin_combination(44)
    nominals = [1, 5, 10, 25]

    value = sum([coins[i] * nominals[i] for i in range(4)])

    assert (
        value == 44
    ), "test_the_sum_of_all_coins_should_be_equal_cents_value"


def test_pennies_should_be_equal_to_remainder_of_cent_division_by_5(
) -> None:

    assert (
        get_coin_combination(59)[0] == 59 % 5
    ), "pennies_should_be_equal_to_remainder_of_cent_division_by_5"


def test_nickels_should_be_less_2_and_equal_to_cent_integer_division_by_5(
) -> None:

    assert (
        get_coin_combination(44)[1] == ((44 // 5) % 5) % 2
    ), "nickels_should_be_less_than_2_and_equal_to_cent_integer_division_by_5"


def test_dimes_should_be_less_3_and_equal_to_cent_integer_division_by_10(
) -> None:

    assert (
        get_coin_combination(44)[2] == ((44 // 5) % 5) // 2
    ), "dimes_should_be_less_3_and_equal_to_cent_integer_division_by_10"


def test_quarters_should_be_equal_to_cent_integer_division_by_25(
) -> None:

    assert (
        get_coin_combination(76)[3] == 76 // 25
    ), "quarters_should_be_equal_to_cent_integer_division_by_25"
