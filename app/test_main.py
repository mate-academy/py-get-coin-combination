import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="test 1 cent"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="task should return 1 penny and 1 nickel"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="task should return 2 pennies, 1 nickel, 1 dime"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="task should return 2 quarters"
        ),
    ]
)
def test_get_coin_combination(cents: int, coins: list[int]) -> None:
    assert get_coin_combination(cents) == coins
