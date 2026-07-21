import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "total_coins,result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test should return penny"
        ),
        pytest.param(
            16,
            [1, 1, 1, 0],
            id="test should return penny, nickel and dime"
        ),
        pytest.param(
            250,
            [0, 0, 0, 10],
            id="test should return only quarters"
        ),
        pytest.param(
            248,
            [3, 0, 2, 9],
            id="test should return pennies, dimes, quarters"
        )
    ]
)
def test_should_return_correctly(total_coins: int, result: list) -> None:
    assert get_coin_combination(total_coins) == result
