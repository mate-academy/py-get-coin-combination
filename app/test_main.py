import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coin_combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (47, [2, 0, 2, 1])
    ]
)
def test_get_coin_combination(cents: int, coin_combination: list) -> None:
    assert get_coin_combination(cents) == coin_combination


def test_raising_error_correctly() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")
