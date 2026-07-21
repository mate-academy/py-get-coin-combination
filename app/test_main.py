import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (0, [0, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (17, [2, 1, 1, 0]),
    ])
def test_get_coin_combination(cents: int, result: list) -> None:
    assert (get_coin_combination(cents) == result)


# def test_get_coin_combination_error() -> None:
#     with pytest.raises(Exception):
#         get_coin_combination(-12)
