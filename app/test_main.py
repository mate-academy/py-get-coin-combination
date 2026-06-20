import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),          # no coins
        (1, [1, 0, 0, 0]),          # 1 penny
        (5, [0, 1, 0, 0]),          # 1 nickel
        (10, [0, 0, 1, 0]),         # 1 dime
        (25, [0, 0, 0, 1]),         # 1 quarter
        (6, [1, 1, 0, 0]),          # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),         # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),         # 2 quarters
        (99, [4, 0, 2, 3]),         # 3 quarters + 2 dimes + 4 pennies
    ],
)
def test_examples(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_monotonic_increase() -> None:
    """Ensure coin combination always sums to the correct value."""
    for cents in range(1, 100):
        combo = get_coin_combination(cents)
        # Перевіряємо, що всі значення невід’ємні
        assert all(c >= 0 for c in combo)
        # Перевіряємо, що сума монет дорівнює потрібній кількості центів
        total = combo[0] + combo[1] * 5 + combo[2] * 10 + combo[3] * 25
        assert total == cents



def test_large_value() -> None:
    """Check a large amount like 1000 cents (10 dollars)."""
    result = get_coin_combination(1000)
    # 40 quarters, no other coins
    assert result == [0, 0, 0, 40]


def test_invalid_type() -> None:
    """Passing noninteger should raise TypeError."""
    with pytest.raises(TypeError):
        get_coin_combination("ten")  # type: ignore
