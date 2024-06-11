import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 cent should equal to 1 penny",
        "6 cents should equal to 1 nickel and 1 penny",
        "17 cents should equal to 1 dime, 1 nickel and 2 cents",
        "50 cents should equal to 2 quarters"
    ]
)
def test_test_cents_separations(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result
