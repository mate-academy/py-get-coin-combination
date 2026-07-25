import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(0, [0, 0, 0, 0]),
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(5, [0, 1, 0, 0]),
        pytest.param(10, [0, 0, 1, 0]),
        pytest.param(25, [0, 0, 0, 1]),

        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(16, [1, 1, 1, 0]),
        pytest.param(41, [1, 1, 1, 1]),

        pytest.param(26, [1, 0, 0, 1]),
        pytest.param(31, [1, 1, 0, 1]),
        pytest.param(30, [0, 1, 0, 1]),
        pytest.param(100, [0, 0, 0, 4]),

    ])
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
