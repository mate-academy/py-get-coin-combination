import pytest
from random import randint

from app.main import get_coin_combination


@pytest.mark.parametrize("coins,exception", [
    ("1", TypeError),
    ([1], TypeError),
    (-1, ValueError),
])
def test_func_should_raise_correct_exception(
        coins: int,
        exception: Exception
) -> None:
    with pytest.raises(exception):
        assert get_coin_combination(coins)


@pytest.mark.parametrize("coins,datatype", [
    (0, list),
    (10, list),
    (1000, list),
])
def test_func_should_return_correct_type(
        coins: int,
        datatype: type
) -> None:
    value = get_coin_combination(coins)
    assert isinstance(value, datatype)


@pytest.mark.parametrize("coins,expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (15, [0, 1, 1, 0]),
    (16, [1, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (35, [0, 0, 1, 1]),
    (40, [0, 1, 1, 1]),
    (41, [1, 1, 1, 1]),
    (183, [3, 1, 0, 7]),
    (189, [4, 0, 1, 7]),
    (192, [2, 1, 1, 7]),
    (199, [4, 0, 2, 7]),
])
def test_func_should_return_correct_list(
        coins: int,
        expected: list[int]
) -> None:
    value = get_coin_combination(coins)
    assert value == expected


@pytest.mark.parametrize("coins", [
    (randint(0, 10000)),
    (randint(0, 10000)),
    (randint(0, 10000)),
    (randint(0, 10000)),
    (randint(0, 10000)),
    (randint(0, 10000)),
    (randint(0, 10000)),
    (randint(0, 10000)),
    (randint(0, 10000)),
    (randint(0, 10000))
])
def test_func_should_return_items_with_random(
        coins: int,
) -> None:
    value = get_coin_combination(coins)
    pennies, nickels, dimes, _ = value
    assert pennies < 5
    assert nickels < 2
    assert dimes < 3
