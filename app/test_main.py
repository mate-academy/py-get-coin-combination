from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    ("cents", "expected_list_of_coins"),
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="list should contain zeros if `cents` equals 0"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="list should contain different types of coins"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="list should contain penny, nickel and dime"
        )
    ]
)
def test_correct_coin_combination(
        cents: int,
        expected_list_of_coins: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_list_of_coins
