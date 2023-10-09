import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 cent",
        "6 cents",
        "17 cents",
        "50 cents"
    ]
)
def test_number_of_coins(value: int, result: list) -> None:
    assert get_coin_combination(value) == result
