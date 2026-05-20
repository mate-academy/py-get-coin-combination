import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "init_cents, returned_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (7, [2, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_coin_comb(init_cents: int, returned_result: list) -> None:
    result = get_coin_combination(init_cents)
    assert result == returned_result
