from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, list_of_value", [
    (0, [0, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (16, [1, 1, 1, 0]),
    (41, [1, 1, 1, 1])
])
def test_get_coin_combination(cents: int, list_of_value: list) -> None:
    assert get_coin_combination(cents) == list_of_value
