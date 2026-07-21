import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent,result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="must work with zero"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="must work when 2 quarters"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="must work when 2 pennies + 1 nickel + 1 dime"
        )
    ]
)
def test_checking_money(cent: int, result: list[int]) -> None:
    assert get_coin_combination(cent) == result
