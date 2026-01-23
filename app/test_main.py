import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(
            0, [0, 0 ,0 ,0],
            id="Return Zero coins"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="Return one coin"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="Return 10 coins"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="Return 17 coins"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="Return 50 coins"
        ),
        pytest.param(
            100, [0, 0, 0, 4],
            id="Return 100 coins"
        )

    ]
)
def test_get_coin_combination(
        cents: int,
        coins: list[int],
)-> None:
    assert get_coin_combination(cents) == coins