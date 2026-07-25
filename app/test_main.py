import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,extended_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_possible_number_of_coins(
        cents: int,
        extended_result: list[int]
) -> None:
    assert get_coin_combination(cents) == extended_result
