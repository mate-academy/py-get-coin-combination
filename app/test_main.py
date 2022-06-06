import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (50, [0, 0, 0, 2]),
        (67, [2, 1, 1, 2]),
        (0, [0, 0, 0, 0]),
        (6, [1, 1, 0, 0])
    ],
)
def tests_get_coin_combination(cents, result):
    assert get_coin_combination(cents) == result, (
        f"Function should return {result}, when cents are equal to {cents}"
    )
