import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero amount"),
        pytest.param(1, [1, 0, 0, 0], id="one cent"),
        pytest.param(5, [0, 1, 0, 0], id="five cents"),
        pytest.param(10, [0, 0, 1, 0], id="ten cents"),
        pytest.param(25, [0, 0, 0, 1], id="twenty-five cents"),
        pytest.param(6, [1, 1, 0, 0], id="six cents"),
        pytest.param(11, [1, 0, 1, 0], id="eleven cents"),
        pytest.param(17, [2, 1, 1, 0], id="seventeen cents"),
        pytest.param(30, [0, 1, 0, 1], id="thirty cents"),
        pytest.param(99, [4, 0, 2, 3], id="ninety-nine cents"),
    ]
)
def test_get_coin_combination(amount: int, expected: list) -> None:
    result = get_coin_combination(amount)
    assert result == expected
