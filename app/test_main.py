import pytest
from app.main import get_coin_combination


# write your tests here
@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (26, [1, 0, 0, 1]),
    ],
    ids=[
        "Should return all 0 if cents is 0",
        "Should return 1 penny if cents is 1",
        "Should return 1 nickels and 1 pennie if cents is 6",
        "Should return 1 dime, 1 nickels and 2 pennie if cents is 17",
        "Should return 2 quarters if cents is 50",
        "Should return 1 quarters and 1 pennie if cents is 26",
    ]
)
def test_function_should_calculate_correctly(cents: int, result: list) -> None:
    assert (get_coin_combination(cents) == result)
