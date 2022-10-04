from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected", [
        pytest.param(0,
                     [0, 0, 0, 0],
                     id="should return zero"),
        pytest.param(1,
                     [1, 0, 0, 0],
                     id="should return penny"),
        pytest.param(7,
                     [2, 1, 0, 0],
                     id="should return two pennies and nickel"),
        pytest.param(19,
                     [4, 1, 1, 0],
                     id="should return four pennies, nickel and dime"),
        pytest.param(40,
                     [0, 1, 1, 1],
                     id="should return nickel, dime and quarter"),
        pytest.param(116,
                     [1, 1, 1, 4],
                     id="should return penny, nickel, dime and four quarters"),
        pytest.param(2525,
                     [0, 0, 0, 101],
                     id="should return many quarters")
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected
