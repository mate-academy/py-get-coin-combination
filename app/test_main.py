import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (0, [0, 0, 0, 0]),
        (46, [1, 0, 2, 1]),
        (100, [0, 0, 0, 4]),
        (34532, [2, 1, 0, 1381]),
    ],
    ids=[
        "test for 1 cent",
        "test for 5 cents",
        "test for 10 cents",
        "test for 25 cents",
        "test for 0 cents",
        "test for 46 cents",
        "test for 100 cents",
        "test for 34532 cents",
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
