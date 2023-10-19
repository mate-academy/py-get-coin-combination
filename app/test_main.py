import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coin_combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_return_coin_combination(cents: int,
                                 coin_combination: list[int]) -> None:
    assert get_coin_combination(cents) == coin_combination
