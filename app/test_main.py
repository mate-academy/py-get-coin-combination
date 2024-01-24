import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("amount, expected_result", [
    (1, [1, 0, 0, 0]),
    (3, [3, 0, 0, 0]),
    (10, [10, 0, 0, 0]),
])
def test_get_coin_combination_pennies(amount, expected_result) -> None:
    assert get_coin_combination(amount) == expected_result


@pytest.mark.parametrize("amount, expected_result", [
    (5, [0, 1, 0, 0]),
    (15, [0, 3, 0, 0]),
])
def test_get_coin_combination_nickels(amount, expected_result) -> None:
    assert get_coin_combination(amount) == expected_result


@pytest.mark.parametrize("amount, expected_result", [
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 2, 0]),
])
def test_get_coin_combination_dimes(amount, expected_result) -> None:
    assert get_coin_combination(amount) == expected_result


@pytest.mark.parametrize("amount, expected_result", [
    (25, [0, 0, 0, 1]),
    (100, [0, 0, 0, 4]),
])
def test_get_coin_combination_quarters(amount, expected_result) -> None:
    assert get_coin_combination(amount) == expected_result


@pytest.mark.parametrize("amount, expected_result", [
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
])
def test_get_coin_combination_mixed(amount, expected_result) -> None:
    assert get_coin_combination(amount) == expected_result
