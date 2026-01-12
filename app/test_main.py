import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,resul",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_get_coin_combination(cents: int, resul: list) -> None:
    assert get_coin_combination(cents) == resul
