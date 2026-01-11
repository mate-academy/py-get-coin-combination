import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0],
                     id="all coins should be 0 when cents is 0"),
        pytest.param(1, [1, 0, 0, 0],
                     id="pennies should be 1 when cents is 1"),
        pytest.param(5, [0, 1, 0, 0],
                     id="nickels should be 1 when cents is 5"),
        pytest.param(10, [0, 0, 1, 0],
                     id="dimes should be 1 when cents is 10"),
        pytest.param(25, [0, 0, 0, 1],
                     id="quarters should be 1 when cents is 25"),
        pytest.param(17, [2, 1, 1, 0],
                     id="should return different types of coins "
                        "when cents is not 0, 1, 5, 10, 25")
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
