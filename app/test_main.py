import pytest

from app.main import get_coin_combination


def test_return_list() -> None:
    assert isinstance(get_coin_combination(4), list)


@pytest.mark.parametrize(
    "amount, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "should return zero",
        "Should return 1 penny",
        "Should return 1 penny and 1 nickel",
        "Should return 2 pennies, 1 nickel and 1 dime",
        "Should return 2 quarters"
    ]
)
def test_return_smallest_result(amount: int,
                                expected_result: list
                                ) -> None:
    assert get_coin_combination(amount) == expected_result
