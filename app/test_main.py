import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            0, [0, 0, 0, 0], id="0 cents should return 0 coin"
        ),
        pytest.param(
            1, [1, 0, 0, 0], id="1 cents should return 1 penny"
        ),
        pytest.param(
            22, [2, 0, 2, 0], id="22 cents should return 2 dime and 2 penny"
        ),
        pytest.param(
            50, [0, 0, 0, 2], id="50 cents should return 2 quarter "
        ),
        pytest.param(
            52, [2, 0, 0, 2], id="68 cents should return 2 quarter,2 penny"
        ),
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
