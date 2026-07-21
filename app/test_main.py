import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_conversion_of_cents(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), ("Conversion of cents should equal to {result}."
        "Where [penny, nickel, dime, quarters]")
