import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin_amount, expected_result",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="expecting only pennies"),
        pytest.param(6, [1, 1, 0, 0],
                     id="expecting pennies and nickels"),
        pytest.param(17, [2, 1, 1, 0],
                     id="expecting pennies, nickels and dimes"),
        pytest.param(50, [0, 0, 0, 2],
                     id="expecting quarters"),
    ]
)
def test_correct_count(
        coin_amount: int,
        expected_result: list
) -> None:
    assert get_coin_combination(coin_amount) == expected_result
