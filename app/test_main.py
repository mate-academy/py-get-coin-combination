import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0])
    ],
    ids=[
        "1 cent should equal 1 penny",
        "6 cents should equal 1 penny + 1 nickel",
        "17 cents should equal 2 pennies + 1 nickel + 1 dime",
        "50 cents should equal 2 quarters",
        "returns list with zeros when cents = 0"
    ]
)
def test_returns_correct_result(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        (-5, ValueError)
    ],
    ids=[
        "should raise ValueError when receives negative parameter"
    ]
)
def test_if_func_raises_correct_error(
        cents: int,
        expected_error: BaseException
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
