import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (90, [0, 1, 1, 3]),
        (10000, [0, 0, 0, 400])
    ],
    ids=[
        "check 0",
        "check 1",
        "check 5",
        "check 10",
        "check 25",
        "check 6",
        "check 17",
        "check 30",
        "check 50",
        "check 90",
        "check extra large 10000"
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("a")
