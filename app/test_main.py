import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin_amount, expected_result",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="should return 1 penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="should return 1 penny + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0],
                     id="should return 2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2],
                     id="should return 2 quarters"),
        pytest.param(167, [2, 1, 1, 6],
                     id="should return all types of coins together"),
        pytest.param(0, [0, 0, 0, 0],
                     id="should return all zeroes"),
    ]
)
def test_should_return_proper_coin_combination(coin_amount: int,
                                               expected_result: list
                                               ) -> None:
    assert get_coin_combination(coin_amount) == expected_result


def test_cents_type_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("100")
