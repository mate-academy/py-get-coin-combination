import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero cents"),
        pytest.param(1, [1, 0, 0, 0], id="one penny"),
        pytest.param(4, [4, 0, 0, 0], id="four pennies"),
        pytest.param(5, [0, 1, 0, 0], id="one nickel"),
        pytest.param(6, [1, 1, 0, 0], id="one penny and 1 nickel"),
        pytest.param(10, [0, 0, 1, 0], id="one dime"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(24, [4, 0, 2, 0], id="4 pennies and  2 dimes"),
        pytest.param(25, [0, 0, 0, 1], id="one quarter"),
        pytest.param(41, [1, 1, 1, 1], id="all coins test"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
        pytest.param(101, [1, 0, 0, 4], id="4 quarters and 1 penny")
    ]
)
def test_get_coin_combination_different_cases(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected
