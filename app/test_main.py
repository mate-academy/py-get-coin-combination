import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return one penny coin when argument is 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return 1 penny/1 nickel coin when argument is 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return 2 penny/1 nickel/1 dime coin when argument is 17"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should return 1 kind of every coin when argument is 41"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return 2 quarters coin when argument is 50"
        )
    ]
)
def test_coin_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result
