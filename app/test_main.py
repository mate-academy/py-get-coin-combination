import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coin_combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (68, [3, 1, 1, 2])
    ]
)
def test_got_coins_combination_correctly(
        cents: int,
        coin_combination: list[int]
) -> None:
    assert get_coin_combination(cents) == coin_combination
