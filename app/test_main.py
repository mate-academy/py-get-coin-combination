import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "should return all zeros",
        "should return 1 penny",
        "should return 1 penny + 1 nickel",
        "should return 2 pennies + 1 nickel + 1 dime",
        "should return 2 quarters",
    ]
)
def test_coin_combination(cents: int, combination: list[int]) -> None:
    assert get_coin_combination(cents) == combination


@pytest.mark.parametrize(
    "cents",
    [
        "five",
        [5],
    ],
    ids=[
        "should raise error if cent type is string",
        "should raise error if cent type is list",
    ]
)
def test_raise_errors_correctly(
        cents: int
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
