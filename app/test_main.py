import pytest
from app.main import get_coin_combination

# 1 penny = 1 cent;
# 1 nickel = 5 cents;
# 1 dime = 10 cents;
# 1 quarter = 25 cents


# write your tests here
@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (66, [1, 1, 1, 2])
    ]
)
def test_cent_counter(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
