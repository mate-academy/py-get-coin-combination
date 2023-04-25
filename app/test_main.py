import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_value, result_coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        pytest.param(0, [0, 0, 0, 0], id="null check"),
        pytest.param(9148, [3, 0, 2, 365], id="high values check")
    ]
)
def test_get_coin_combination_with_non_negative_integer(
        cents_value: int,
        result_coins: list
) -> None:
    assert get_coin_combination(cents_value) == result_coins
