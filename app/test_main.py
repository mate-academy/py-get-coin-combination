import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result", [
        pytest.param(4, [4, 0, 0, 0],
                     id="one type of coins"),
        pytest.param(9, [4, 1, 0, 0],
                     id="two types of coins"),
        pytest.param(18, [3, 1, 1, 0],
                     id="three types of coins"),
        pytest.param(118, [3, 1, 1, 4],
                     id="four types of coins")
    ]
)
def test_get_coin_combination(
        cents: int,
        result: list
) -> None:
    assert (
        get_coin_combination(cents) == result
    )
