import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "number_of_cents,expected_coin_combination",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="correctly_handle_zero_coins"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="1 cent should be 1 penny"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="5 cents should be 1 nickel"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="10 cents should be 1 dime"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="25 cents should be 1 quarter"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="every nominal should be"
        ),
        pytest.param(
            137,
            [2, 0, 1, 5],
            id="big amount of coins"
        )
    ]
)
def test_get_coin_combination(
    number_of_cents: int,
    expected_coin_combination: list[int]
) -> None:
    assert (
        get_coin_combination(number_of_cents)
        == expected_coin_combination
    )
