import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero cents"),
        pytest.param(1, [1, 0, 0, 0], id="single penny"),
        pytest.param(5, [0, 1, 0, 0], id="single nickel"),
        pytest.param(10, [0, 0, 1, 0], id="single dime"),
        pytest.param(25, [0, 0, 0, 1], id="single quarter"),
    ],
)
def test_single_coin_cases(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(6, [1, 1, 0, 0], id="penny and nickel"),
        pytest.param(17, [2, 1, 1, 0], id="pennies, nickel and dime"),
        pytest.param(50, [0, 0, 0, 2], id="two quarters"),
        pytest.param(99, [4, 0, 2, 3], id="pennies, dimes and quarters"),
    ],
)
def test_mixed_coin_cases(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(100, [0, 0, 0, 4], id="four quarters"),
        pytest.param(1000, [0, 0, 0, 40], id="forty quarters"),
    ],
)
def test_large_amounts(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
