import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="test zero cents"),
        pytest.param(1, [1, 0, 0, 0], id="test 1 cent - only pennies"),
        pytest.param(5, [0, 1, 0, 0], id="test 5 cents - only nickels"),
        pytest.param(10, [0, 0, 1, 0], id="test 10 cents - only dimes"),
        pytest.param(25, [0, 0, 0, 1], id="test 25 cents - only quarters"),

        pytest.param(2, [2, 0, 0, 0], id="test multiple pennies"),
        pytest.param(15, [0, 1, 1, 0], id="test multiple nickels"),
        pytest.param(30, [0, 1, 0, 1], id="test multiple dimes"),
        pytest.param(75, [0, 0, 0, 3], id="test multiple quarters"),

        pytest.param(6, [1, 1, 0, 0], id="test 6 cents"),
        pytest.param(41, [1, 1, 1, 1], id="test all coins"),
        pytest.param(67, [2, 1, 1, 2], id="test complex combination"),
        pytest.param(99, [4, 0, 2, 3], id="test 99 cents"),


        pytest.param(24, [4, 0, 2, 0], id="test just before quarter"),
        pytest.param(50, [0, 0, 0, 2], id="test two quarters"),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
