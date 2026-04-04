from app.main import get_coin_combination
import pytest
from typing import Any

@pytest.mark.parametrize(
    "cents, expected",
    [
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
    ],
)
def test_coin_combinations(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected


def test_negative_raises_value_error() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-100)


@pytest.mark.parametrize("bad_type", [1.5, "10", None, [], {}])
def test_bad_types_raise_type_error(bad_type: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(bad_type)


def test_large_value_performance_and_correctness() -> None:
    cents = 10**6
    result = get_coin_combination(cents)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) and x >= 0 for x in result)
    total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
    assert total == cents
