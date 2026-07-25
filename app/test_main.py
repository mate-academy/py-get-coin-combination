import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
    (41, [1, 1, 1, 1]),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
])
def test_sum_of_coins_equals_cents(cents: int, expected: list) -> None:
    values = [1, 5, 10, 25]
    result = get_coin_combination(cents)
    total = sum(result[i] * values[i] for i in range(4))
    assert total == cents


@pytest.mark.parametrize("cents", [1, 6, 17, 50, 99, 100])
def test_returns_list_of_four_elements(cents: int) -> None:
    assert len(get_coin_combination(cents)) == 4


@pytest.mark.parametrize("cents, expected_invalid", [
    ("10", TypeError),
    (None, TypeError),
    (-1, Exception),
])
def test_invalid_input_raises_exception(
        cents: int,
        expected_invalid: type
) -> None:
    with pytest.raises(expected_invalid):
        get_coin_combination(cents)
