import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (100, [0, 0, 0, 4]),
    ]
)
def test_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
