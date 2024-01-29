import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "number_of_coins,result_list",
    [
        (0, [0, 0, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "should return list with zeros when number of coins is 0",
        "should return different coins when we have a lot of coins",
        "should return [0, 0, 0, 2], when number of coins is 50"
    ]
)
def test_of_combination(number_of_coins: int, result_list: list) -> None:
    assert get_coin_combination(number_of_coins) == result_list

# get_coin_combination(50) == [0, 0, 0, 2]
