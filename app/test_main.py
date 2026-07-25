import pytest

from app.main import get_coin_combination


# values = [1, 5, 10, 25]
@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4])
    ]
)
def test_valid_coin_combos(
    cents: int,
    result: list[int]
) -> None:
    assert (
        get_coin_combination(cents) == result
    ), (f"{cents} cents, should be {result} coins")
