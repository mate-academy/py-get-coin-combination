import pytest
from app.main import get_coin_combination


def test_get_coin_combination_list_large_values() -> None:
    coins = get_coin_combination(17)
    assert isinstance(coins, list)
    assert len(coins) == 4
    assert all(isinstance(x, int) for x in coins)


def test_get_coin_combination_expected_coins() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(99) == [4, 0, 2, 3]
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_get_coin_combination_negative_inputs() -> None:
    try:
        result = get_coin_combination(-1)
        assert result == [4, 0, 2, -1], (
            "Result contains negative values.Return negative inputs"
        )
    except Exception as e:
        pytest.fail(f"Unexpected exception {e}")


@pytest.mark.parametrize("cents, expected", [
    ("ten", TypeError),
    (None, TypeError),
])
def test_get_coin_combination_invalid_inputs(
        cents: int,
        expected: type
) -> None:
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            get_coin_combination(cents)
    else:
        result = get_coin_combination(cents)
        assert result == expected, (
            f"Expected {expected} but got {result} for cents={cents}"
        )
