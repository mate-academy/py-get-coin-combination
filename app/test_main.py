import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (41, [1, 1, 1, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
])
def test_valid_combinations(cents: int, expected: list[int]) -> None:
    result = get_coin_combination(cents)
    assert result == expected,\
        f"For {cents} cents expected {expected}, but got {result}"


def test_large_input() -> None:
    cents = 99999
    result = get_coin_combination(cents)
    total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
    assert total == cents
    assert isinstance(result, list) and len(result) == 4
    for count in result:
        assert isinstance(count, int)
        assert count >= 0


def test_invalid_input_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("50")


def test_negative_input() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-5)
