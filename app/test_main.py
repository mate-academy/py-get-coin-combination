import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="should add penny to the list"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="should add nickel to the list"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="should add dime to the list"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="should add quarters to the list"
        ),
        pytest.param(
            68, [3, 1, 1, 2],
            id="should add different coins to the list"
        ),
        pytest.param(
            0, [0, 0, 0, 0],
            id="should return an empty list"
        ),
    ]
)
def test_get_coin_combination(cents: int,
                              expected_coins: list
                              ) -> None:
    assert get_coin_combination(cents) == expected_coins
