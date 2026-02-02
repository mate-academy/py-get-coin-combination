import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "Should return list of 0 if cent = 0",
        "Should return 1 penny if cent = 1",
        "Should return 1 penny + 1 nickel if cent = 6",
        "Should return 2 penny + 1 nickel + 1 dime if cent = 17",
        "Should return 2 quarters if cent = 50"
    ]
)
def test_should_return_correct_value(cent: int, result: list[int]) -> None:
    assert get_coin_combination(cent) == result
