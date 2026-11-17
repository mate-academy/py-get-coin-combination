import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(1, [1, 0, 0, 0], id="Test with only one cent"),
        pytest.param(4, [4, 0, 0, 0], id="Test with Four cents."),
        pytest.param(5, [0, 1, 0, 0], id="Test with Five cents."),
        pytest.param(9, [4, 1, 0, 0], id="Test with Nine cents."),
        pytest.param(10, [0, 0, 1, 0], id="Test with Ten cents"),
        pytest.param(14, [4, 0, 1, 0], id="Test with 14 cents"),
        pytest.param(15, [0, 1, 1, 0], id="Test with 15 cents."),
        pytest.param(19, [4, 1, 1, 0], id="Test with 19 cents."),
        pytest.param(20, [0, 0, 2, 0], id="Test with 20 cents."),
        pytest.param(24, [4, 0, 2, 0], id="Test with 24 cents."),
        pytest.param(25, [0, 0, 0, 1], id="Test with a quarter")
    ]
)
def test_get_coin_combination(cents: int,
                              coins: list) -> None:
    assert (
        get_coin_combination(cents) == coins
    ), (f"To make {cents} cents you need {coins[0]} pennies,"
        f"{coins[1]} nickels, {coins[2]} dimes and {coins[3]} quarters!")
