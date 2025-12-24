from pytest import mark, param
from app.main import get_coin_combination


@mark.parametrize(
    "cents,expected_result",
    [
        param(1, [1, 0, 0, 0],
              id="should_return_1penny"),
        param(6, [1, 1, 0, 0],
              id="should_return_1penny&1nickel"),
        param(17, [2, 1, 1, 0],
              id="should_return_2pennies&1nickel&1dime"),
        param(50, [0, 0, 0, 2],
              id="should_return_2quarters"),
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
