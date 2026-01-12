import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (7, [2, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (42, [2, 1, 1, 1])
    ],
    ids=[
        "Test failed with 1 cent",
        "Test failed with 8 cents",
        "Test failed with 16 cents",
        "Test failed with 42 cents",
    ]
)
def test_coin_combination_matches(
        cents: int,
        result: list) -> None:
    assert get_coin_combination(cents) == result
