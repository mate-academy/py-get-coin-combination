import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="0 cents should be equal to list with all 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="0 cents should be equal to list with all 0"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="0 cents should be equal to list with all 0"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="0 cents should be equal to list with all 0"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="0 cents should be equal to list with all 0"
        ),
    ]
)
def test_coin_combination(cents: int, expected_coins: list[int]) -> None:
    assert get_coin_combination(cents) == expected_coins
