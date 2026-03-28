import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "one nickel one cent",
        "two cents one nickel one dime",
        "two quarters"
    ]
)
def test_method(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
