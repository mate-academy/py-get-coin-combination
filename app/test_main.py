import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            42,
            [2, 1, 1, 1],
            id="get all type of coins"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="get zero coins"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="get one type of coins"
        )
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
