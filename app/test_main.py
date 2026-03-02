import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        (2, [2, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (8, [3, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (98, [3, 0, 2, 3])
    ], ids=[
        "should return only penny if cents < 5",
        "should return only nickel if cents = 5",
        "should return only penny and nickel if 5 < cents < 10",
        "should return penny, nickel and dime if 10 < cents < 25",
        "should return quarters if cents = 25",
        "should return correct combination if 25 < cents < 100"
    ]
)
def test_should_return_proper_coins_list(
    cents: int, expected_coins: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_coins


def test_should_raise_type_error_when_given_wrong_input() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("3")
