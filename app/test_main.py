import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "returns penny",
        "returns nickel",
        "returns dime",
        "returns quarter"
    ]
)
def test_get_coin_combination(cent: int, result: list) -> None:
    assert get_coin_combination(cent) == result
