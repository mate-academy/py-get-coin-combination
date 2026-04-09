import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_should_return_list_of_length_four() -> None:
    result = get_coin_combination(100)
    assert len(result) == 4


def test_sum_of_coins_should_equal_cents() -> None:
    # Validación de integridad: el valor total debe coincidir con la entrada
    cents = 87
    p, n, d, q = get_coin_combination(cents)
    total = p * 1 + n * 5 + d * 10 + q * 25
    assert total == cents
