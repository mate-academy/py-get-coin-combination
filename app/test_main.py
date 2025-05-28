import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero cents"),
        pytest.param(1, [1, 0, 0, 0], id="only pennies"),
        pytest.param(5, [0, 1, 0, 0], id="exact nickel"),
        pytest.param(10, [0, 0, 1, 0], id="exact dime"),
        pytest.param(25, [0, 0, 0, 1], id="exact quarter"),
        pytest.param(6, [1, 1, 0, 0], id="nickel + penny"),
        pytest.param(17, [2, 1, 1, 0], id="dime + nickel + pennies"),
        pytest.param(49, [4, 0, 2, 1], id="max mix without full 2nd quarter"),
        pytest.param(50, [0, 0, 0, 2], id="two quarters"),
        pytest.param(99, [4, 0, 2, 3], id="complex case under 100"),
        pytest.param(100, [0, 0, 0, 4], id="exact dollar in quarters"),
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
