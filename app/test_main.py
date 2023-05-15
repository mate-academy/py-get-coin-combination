import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(0, [0, 0, 0, 0]),
        pytest.param(4, [4, 0, 0, 0]),
        pytest.param(5, [0, 1, 0, 0]),
        pytest.param(9, [4, 1, 0, 0])
    ]
)
def test_returns_smallest_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
