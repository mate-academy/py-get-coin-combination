import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        # single check for every type
        pytest.param(1, [1, 0, 0, 0], id="case for penny"),
        pytest.param(5, [0, 1, 0, 0], id="case for nickel"),
        pytest.param(10, [0, 0, 1, 0], id="case for dime"),
        pytest.param(25, [0, 0, 0, 1], id="case for quarter"),
        pytest.param(0, [0, 0, 0, 0], id="case for 0 cents"),
        # check for combinations
        pytest.param(15, [0, 1, 1, 0], id="case for nickel+dime"),
        pytest.param(26, [1, 0, 0, 1], id="case for penny+quarter"),
        pytest.param(35, [0, 0, 1, 1], id="case for dime+quarter"),
        pytest.param(6, [1, 1, 0, 0], id="case for penny+nickel"),
        pytest.param(41, [1, 1, 1, 1], id="case for all of coins"),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
