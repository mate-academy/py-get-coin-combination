from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="Test 1: 1 cent = [1, 0, 0, 0]"),
        pytest.param(
            7, [2, 1, 0, 0],
            id="Test 2: 7 cent = [2, 1, 0, 0]"),
        pytest.param(
            18, [3, 1, 1, 0],
            id="Test 3: 18 cent = [3, 1, 1, 0]"),
        pytest.param(
            41, [1, 1, 1, 1],
            id="Test 4: 41 cent = [1, 1, 1, 1]"),
    ]
)
def test_should_return_list_with_1_position(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result
