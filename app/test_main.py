import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="Values should be zeros if it is no cents"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="Only pennies should be if there is less than 5 cents"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="Nickel should be if there is from 5 to 9 cents"
        ),
        pytest.param(
            35, [0, 0, 1, 1],
            id="Quarter should be if there is more than 25 cents"
        ),
    ]
)
def test_count_money_correctly(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result
