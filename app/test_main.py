import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (50, [0, 0, 0, 2]),
    (100, [0, 0, 0, 4])
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [
    (-1),
    (-109000)
])
def test_should_raise_value_error_for_negative_cents(cents: int) -> None:
    with pytest.raises(ValueError) as e:
        get_coin_combination(cents)
    assert str(e.value) == "Cents cannot be negative"
