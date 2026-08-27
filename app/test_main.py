import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zero coins for zero cents"),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return only pennies for small amount"),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return pennies combination"),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return minimum number of coins for mixed amount"),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return multiple quarters for large amount"),
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
