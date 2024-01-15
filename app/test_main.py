from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected_coin_list",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(
        cents: int,
        expected_coin_list: list
) -> None:
    assert (
            get_coin_combination(cents) == expected_coin_list
    ), (f"Combination of {cents} cents should"
        f" be equal to {expected_coin_list}")
