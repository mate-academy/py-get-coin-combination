from __future__ import annotations
from app.main import get_coin_combination
import pytest

def test_should_return_type_list() -> None:
    assert (
        isinstance(get_coin_combination(23), list) is True
    ), "Function 'get_coin_combination' should return list"


@pytest.mark.parametrize(
    "coins_num,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (66, [1, 1, 1, 2])
    ]
)
def test_get_coin_combination(
        coins_num: int,
        result: list[int]
) -> None:
    assert get_coin_combination(coins_num) == result