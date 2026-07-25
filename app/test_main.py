from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,res_list",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
    ]
)
def test_get_coin_combination(cents: int, res_list: list[int]) -> None:
    assert get_coin_combination(cents) == res_list
