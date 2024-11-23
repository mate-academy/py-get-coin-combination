from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents_value, expected_result",
    [
        pytest.param(0, [0, 0, 0, 0], id="cents equal 0"),
        pytest.param(1, [1, 0, 0, 0], id="cents equal 1"),
        pytest.param(10, [0, 0, 1, 0], id="cents equal 10"),
        pytest.param(16, [1, 1, 1, 0], id="cents equal 16"),
        pytest.param(101, [1, 0, 0, 4], id="cents equal 101"),
        pytest.param(1000, [0, 0, 0, 40], id="cents equal 1000"),
    ]
)
def test_get_coin_combination(cents_value: int, expected_result: list) -> None:
    result = get_coin_combination(cents=cents_value)
    assert result == expected_result
