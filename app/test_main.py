import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 coin type"),
        pytest.param(6, [1, 1, 0, 0], id="2 coin type"),
        pytest.param(17, [2, 1, 1, 0], id="3 coin type"),
        pytest.param(41, [1, 1, 1, 1], id="4 coin type"),
        pytest.param(100, [0, 0, 0, 4], id="highest coin type counted first"),
        pytest.param(0, [0, 0, 0, 0], id="zero cents"),

    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
