import pytest
from app.main import get_coin_combination


def test_return_type() -> None:
    assert isinstance(get_coin_combination(1), list)


@pytest.mark.parametrize(
    "amount, expected_result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zero"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="Should be 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="Should be 1 penny + 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="Should be 2 pennies + 1 nickel + 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="Should be 2 quarters"
        )
    ]
)
def test_the_number_of_coins(
        amount: int,
        expected_result: list
) -> None:
    assert get_coin_combination(amount) == expected_result
