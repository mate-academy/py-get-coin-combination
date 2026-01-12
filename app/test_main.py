import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    result = get_coin_combination(cents)
    assert result == expected


def test_get_coin_combination_with_zero_cents() -> None:
    result = get_coin_combination(0)
    assert result == [0, 0, 0, 0]


def test_get_coin_combination_with_large_cents() -> None:
    result = get_coin_combination(1234)
    assert result == [4, 1, 0, 49]
