import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(1, [1, 0, 0, 0], id="check 1 penny test"),
        pytest.param(6, [1, 1, 0, 0], id="check 1 penny + 1 nickle test"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="check 2 quarters test"),
        pytest.param(42, [2, 1, 1, 1], id="check all coins")
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
