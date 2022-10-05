import pytest
from app.main import get_coin_combination


# write your tests here
@pytest.mark.parametrize(
    "cents, list_of_coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return  [0, 0, 0, 0], when input is 0"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return  [0, 0, 0, 0], when input is 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return  [0, 0, 0, 0], when input is 17"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return  [0, 0, 0, 0], when input is 50"
        ),
    ]
)
def test_return_right_coin_combination(cents: int, list_of_coins: list):
    assert get_coin_combination(cents) == list_of_coins
