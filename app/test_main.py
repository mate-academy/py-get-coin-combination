import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("a,result",[
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])]
                         )
def test_list(a: int, result: list[int]) -> None:
   assert (get_coin_combination(a) == result)

