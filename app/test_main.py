import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    ("cents", "expected"),
    [
        pytest.param(0, [0, 0, 0, 0], id="zero cents"),
        pytest.param(1, [1, 0, 0, 0], id="one penny"),
        pytest.param(4, [4, 0, 0, 0], id="before one nickel"),
        pytest.param(5, [0, 1, 0, 0], id="one nickel"),
        pytest.param(6, [1, 1, 0, 0], id="nickel and penny"),
        pytest.param(9, [4, 1, 0, 0], id="before one dime"),
        pytest.param(10, [0, 0, 1, 0], id="one dime"),
        pytest.param(15, [0, 1, 1, 0], id="dime and nickel"),
        pytest.param(24, [4, 0, 2, 0], id="before quarter"),
        pytest.param(25, [0, 0, 0, 1], id="one quarter"),
        pytest.param(26, [1, 0, 0, 1], id="quarter and penny"),
        pytest.param(41, [1, 1, 1, 1], id="all coin types"),
        pytest.param(50, [0, 0, 0, 2], id="two quarters"),
        pytest.param(99, [4, 0, 2, 3], id="large amount with remainder"),
    ],
)
def test_get_coin_combination(
    cents: int,
    expected: list[int],
) -> None:
    assert get_coin_combination(cents=cents) == expected
