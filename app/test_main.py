import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount,result",
    [
        pytest.param(1, [1, 0, 0, 0], id="should convert 5 to 1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="should convert 6 to 1 nickel and 1 penny"),
        pytest.param(17, [2, 1, 1, 0], id="should convert 17 to 1 dime, 1 nickel and 2 penny"),
        pytest.param(50, [0, 0, 0, 2], id="should convert 50 to 2 quarters"),
    ]
)
def test_get_coin_combination(amount: int,  result: list) -> None:
   assert (get_coin_combination(amount) == result)