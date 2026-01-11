import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            1, [1, 0, 0, 0],
        ),

        pytest.param(
            5, [0, 1, 0, 0],
        ),
        pytest.param(
            10, [0, 0, 1, 0],
        ),
        pytest.param(
            25, [0, 0, 0, 1],
        ),
        pytest.param(
            322, [2, 0, 2, 12]
        )
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
