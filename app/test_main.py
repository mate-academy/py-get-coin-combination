import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,list_of_coins",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="For 0 cents should return [0, 0, 0, 0]"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="For 1 cent should return [1, 0, 0, 0]"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="For 6 cents should return [1, 1, 0, 0]"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="For 17 cents should return [2, 1, 1, 0]"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="For 50 cents should return [0, 0, 0, 2]"
        ),

    ]
)
def test_get_coin_combination(cents: int, list_of_coins: list) -> None:
    assert get_coin_combination(cents) == list_of_coins
