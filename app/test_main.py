import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="0 cents should return list of 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="1 cent should return 1 penny"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="6 cents should return 1 penny and 1 nickel"
        ),
        pytest.param(
            15, [0, 1, 1, 0],
            id="15 cents should return 1 nickel and 1 pennies"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="17 cents should return 2 pennies, 1 nickel and 1 dime"
        ),
        pytest.param(
            20, [0, 0, 2, 0],
            id="20 cents should return 2 dimes"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="50 cents should return 2 quarters"
        ),
        pytest.param(
            226, [1, 0, 0, 9],
            id="226 cents should return 9 quarters and 1 penny"
        ),
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
