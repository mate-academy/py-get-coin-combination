import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0],
                     id="should return zero coins for zero cents"),
        pytest.param(1, [1, 0, 0, 0],
                     id="should return only pennies for small amount"),
        pytest.param(4, [4, 0, 0, 0],
                     id="should return pennies combination "
                        "before nickel transition"),
        pytest.param(5, [0, 1, 0, 0],
                     id="should return combination after nickel transition"),
        pytest.param(9, [4, 1, 0, 0],
                     id="should return combination before dime transition"),
        pytest.param(10, [0, 0, 1, 0],
                     id="should return combination after dime transition"),
        pytest.param(24, [4, 0, 2, 0],
                     id="should return combination before quarter transition"),
        pytest.param(25, [0, 0, 0, 1],
                     id="should return combination after quarter transition"),
        pytest.param(29, [4, 0, 0, 1],
                     id="should return minimum coins "
                        "after quarter transition"),
        pytest.param(99, [4, 0, 2, 3],
                     id="should return multiple quarters for large amount"),
        pytest.param(17, [2, 1, 1, 0],
                     id="should return minimum number "
                        "of coins for mixed amount"),
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
