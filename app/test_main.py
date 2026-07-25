import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "0 cents should return [0, 0, 0, 0]",
        "1 cents should return [1, 0, 0, 0]",
        "6 cents should return [1, 1, 0, 0]",
        "17 cents should return [2, 1, 1, 0]",
        "50 cents should return [0, 0, 0, 2]"
    ]
)
def test_coin_coin_combinations(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
