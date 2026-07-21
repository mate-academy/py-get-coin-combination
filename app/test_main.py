from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("amount, result", [
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (41, [1, 1, 1, 1]),
    (146, [1, 0, 2, 5])])
def test_action(amount: int, result: list) -> None:
    assert get_coin_combination(amount) == result
