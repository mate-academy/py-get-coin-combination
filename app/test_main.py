import pytest

from typing import List

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (100, [0, 0, 0, 4]),
        (63, [3, 0, 1, 2]),
        (0, [0, 0, 0, 0]),
    ],
    ids=[
        "Should return correct amount for penny",
        "Should return correct amount for nickle",
        "Should return correct amount for dime",
        "Should return correct amount for quarter",
        "Should return correct amount for dollar",
        "Should return correct amount",
        "Should return zero if zero cents given",
    ]
)
def test_should_return_correct_ammount(
        cents: int,
        expected_result: List[int]
) -> None:

    assert get_coin_combination(cents) == expected_result
