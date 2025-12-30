import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(1, [1, 0, 0, 0], id="one_cent"),
        pytest.param(6, [1, 1, 0, 0], id="six_cents"),
        pytest.param(17, [2, 1, 1, 0], id="seventeen_cents"),
        pytest.param(50, [0, 0, 0, 2], id="fifty_cents"),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
