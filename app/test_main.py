import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    pytest.param(1, [1, 0, 0, 0], id="test should return (1 penny = 1 cent)"),
    pytest.param(5, [0, 1, 0, 0],
                 id="test should return (1 nickel = 5 cents)"),
    pytest.param(10, [0, 0, 1, 0],
                 id="test should return (1 dime = 10 cents)"),
    pytest.param(25, [0, 0, 0, 1],
                 id="test should return (1 quarter = 25 cents)"),
    pytest.param(26, [1, 0, 0, 1],
                 id="test should return 1 penny and 1 quarter"),
    pytest.param(31, [1, 1, 0, 1],
                 id="test should return 1 penny, 1 nickel and 1 quarters"),
    pytest.param(41, [1, 1, 1, 1],
                 id="test should return 1 penny,"
                    " 1 nickel, 1 dimes and 1 quarters"),

]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert (
        get_coin_combination(cents) == expected
    )
