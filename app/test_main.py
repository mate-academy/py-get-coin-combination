from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected_result", [
    pytest.param(0, [0, 0, 0, 0]),
    pytest.param(5, [0, 1, 0, 0]),
    pytest.param(10, [0, 0, 1, 0]),
    pytest.param(17, [2, 1, 1, 0]),
])
def test_get_coin_combination_good(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
