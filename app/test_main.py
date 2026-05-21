import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0,[0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (26, [1, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2])
    ]
)
def test_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected

def test_needs_to_return_a_list_of_types() -> None:
    assert (
        isinstance(get_coin_combination(41), list)  is True
    ), "The 'get_coin_combination' function will return a list"
