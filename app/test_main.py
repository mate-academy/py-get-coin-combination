import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_results",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "zero cents",
        "1 cent",
        "6 cents",
        "17 cents",
        "50 cents, yo"
    ]
)
def test_get_coin_combination(
        cents: int,
        expected_results: list
) -> None:
    assert get_coin_combination(cents) == expected_results
