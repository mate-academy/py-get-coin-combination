from typing import List, Any
import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("amount_of_count, expected_result", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (100, [0, 0, 0, 4]),
    (0, [0, 0, 0, 0]),
    (10000, [0, 0, 0, 400]),
])
def test_get_coin_combination(amount_of_count: int,
                              expected_result: List[int]) -> None:
    assert expected_result == get_coin_combination(amount_of_count)


@pytest.mark.parametrize("invalid_input", [
    "10",
    [10],
    None,
])
def test_get_type_error(invalid_input: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(invalid_input)
