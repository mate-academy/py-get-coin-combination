import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin_combination, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 penny",
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime",
        "2 quarters"
    ]
)
def test_get_coin_combination(coin_combination: int, result: list) -> None:
    assert get_coin_combination(coin_combination) == result
