from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "money, expected",
    [
        pytest.param(1, [1, 0, 0, 0], id="should return 1 penny "),
        pytest.param(6, [1, 1, 0, 0], id="should return penny and nickel"),
        pytest.param(17, [2, 1, 1, 0], id="should return any money"),
        pytest.param(50, [0, 0, 0, 2], id="should return 2 quarter"),
    ]
)
def test_check_param(money: int, expected: list) -> None:
    result = get_coin_combination(money)
    assert result == expected
