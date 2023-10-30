import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_should_return_expected_combinations(
        amount: int,
        expected: list
) -> None:
    assert expected == get_coin_combination(amount)
