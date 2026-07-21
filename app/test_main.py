import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="1 cent should be equal 1 cent"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="17 cents should be equal 2 pennies + 1 nickel + 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="50 cents should be equal 2 quarters"
        )
    ]
)
def test_if_output_is_correct(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result
