import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_value",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "The function could return pennie",
        "The function could return nickel and pennie",
        "The function could return dime, nickel and pennie",
        "The function could return quarter"
    ]

)
def test_word_check_for_repeated_letters(
        cents: int,
        expected_value: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_value
