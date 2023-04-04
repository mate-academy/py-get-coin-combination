from app.main import get_coin_combination
import pytest


def test_should_return_type_list() -> None:
    assert (
        isinstance(get_coin_combination(23), list) is True
    ), "Function should return list"


@pytest.mark.parametrize(
    "cents_int, cents_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (18, [3, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (35, [0, 0, 1, 1]),
        (52, [2, 0, 0, 2]),
        (76, [1, 0, 0, 3]),
        (100, [0, 0, 0, 4]),
        (964, [4, 0, 1, 38]),
        (4653, [3, 0, 0, 186]),
        (78655, [0, 1, 0, 3146]),
        (345875, [0, 0, 0, 13835]),
    ],
)
def test_coin_combination(cents_int: int, cents_list: list) -> None:
    assert get_coin_combination(cents_int) == cents_list, (
        f"Function should return {cents_list} "
        f"when value is {cents_int}"
    )
