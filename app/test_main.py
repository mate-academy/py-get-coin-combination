import pytest
from app.coin_combination import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),    # Zero centavos
        (1, [1, 0, 0, 0]),    # 1 penny
        (4, [4, 0, 0, 0]),    # Apenas pennies
        (5, [0, 1, 0, 0]),    # Exatamente 1 nickel
        (6, [1, 1, 0, 0]),    # 1 penny + 1 nickel
        (10, [0, 0, 1, 0]),   # Exatamente 1 dime
        (17, [2, 1, 1, 0]),   # 2 pennies + 1 nickel + 1 dime
        (25, [0, 0, 0, 1]),   # Exatamente 1 quarter
        (41, [1, 1, 1, 1]),   # Combinação de todas as moedas (1q + 1d + 1n + 1p)
        (50, [0, 0, 0, 2]),   # 2 quarters
        (99, [4, 0, 2, 3]),   # 3 quarters + 2 dimes + 4 pennies
        (100, [0, 0, 0, 4]),  # 4 quarters (1 dólar)
    ],
)
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected
