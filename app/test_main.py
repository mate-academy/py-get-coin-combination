import pytest

from app.main import get_coin_combination


# write your tests here
@pytest.mark.parametrize(
    "income,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0])
    ]
)
def test_get_coin_combination(income: int, result: list) -> None:
    assert (get_coin_combination(income) == result)
