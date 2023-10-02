import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected_result", [
    (1, [1, 0, 0, 0]),  # 1 penny
    (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
    (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
    (50, [0, 0, 0, 2]),  # 2 quarters
])
def test_get_coin_combination(cents, expected_result) -> None:
    assert get_coin_combination(cents) == expected_result
